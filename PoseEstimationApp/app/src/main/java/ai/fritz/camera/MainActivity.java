package ai.fritz.camera;

import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Color;
import android.graphics.Matrix;
import android.hardware.Camera;
import android.media.Image;
import android.media.ImageReader;
import android.os.Build;
import android.os.Bundle;
import android.renderscript.Element;
import android.support.annotation.RequiresApi;
import android.util.Log;
import android.util.Size;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.ProgressBar;
import android.widget.RelativeLayout;
import org.tensorflow.lite.support.image.ImageProcessor;
import org.tensorflow.lite.support.image.TensorImage;
import org.tensorflow.lite.support.image.ops.ResizeOp;
import org.tensorflow.lite.support.tensorbuffer.TensorBuffer;
import android.media.Image.Plane;

import java.io.FileOutputStream;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.concurrent.atomic.AtomicBoolean;

import ai.fritz.core.Fritz;
import ai.fritz.core.FritzOnDeviceModel;
import ai.fritz.core.FritzTFLiteInterpreter;
import ai.fritz.telepathActivities.R;
import ai.fritz.vision.ByteImage;
import ai.fritz.vision.FritzVisionImage;
import ai.fritz.vision.FritzVisionOrientation;
import ai.fritz.vision.ImageOrientation;
import ai.fritz.vision.poseestimation.FritzVisionPosePredictor;
import ai.fritz.vision.poseestimation.FritzVisionPoseResult;
import ai.fritz.vision.poseestimation.Pose;


public class MainActivity extends BaseCameraActivity implements ImageReader.OnImageAvailableListener {

    private static final Size DESIRED_PREVIEW_SIZE = new Size(1280, 960);
    private int yRowStride;
    private AtomicBoolean isComputing = new AtomicBoolean(false);
    private AtomicBoolean shouldSample = new AtomicBoolean(true);
    private ImageOrientation orientation;
    private byte[][] yuvBytes = new byte[3][];

    FritzVisionPoseResult poseResult;
    FritzVisionPosePredictor predictor;
    FritzVisionImage visionImage;

    // Preview Frame
    RelativeLayout previewFrame;
    Button snapshotButton;
    Button snapshotButton2;
    ProgressBar snapshotProcessingSpinner;

    // Snapshot Frame
    RelativeLayout snapshotFrame;
    OverlayView snapshotOverlay;
    Button closeButton;
    Button recordButton;
    ProgressBar recordSpinner;
    FritzTFLiteInterpreter interpreter;

    @Override
    public void onCreate(final Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Fritz.configure(this, "e5196d42e8744211a48caada96b4a649");

        // The code below loads a custom trained pose estimation model and creates a predictor that will be used to identify poses in live video.
        // Custom pose estimation models can be trained with the Fritz AI platform. To use a pre-trained pose estimation model,
        // see the FritzAIStudio demo in this repo.
        FritzOnDeviceModel onDeviceModel = new FritzOnDeviceModel("file:///android_asset/converted_model.tflite", "a418b017c4f546cf910e744278185a6e", 1);
        interpreter = new FritzTFLiteInterpreter(onDeviceModel);
    }


    @Override
    protected int getLayoutId() {
        return R.layout.main_camera;
    }

    @Override
    protected Size getDesiredPreviewFrameSize() {
        return DESIRED_PREVIEW_SIZE;
    }
    private void goHome(){
        Intent intent = new Intent(this, ai.fritz.telepathActivities.home_activity.class);
        startActivity(intent);
    }
    @Override
    public void onPreviewSizeChosen(final Size previewSize, final Size cameraViewSize, final int rotation) {
        orientation = FritzVisionOrientation.getImageOrientationFromCamera(this, cameraId);

        // Preview View
        previewFrame = findViewById(R.id.preview_frame);
        snapshotProcessingSpinner = findViewById(R.id.snapshot_spinner);
        snapshotButton = findViewById(R.id.take_picture_btn);
        snapshotButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               goHome();
            }
        });
        snapshotButton2 = findViewById(R.id.take_picture_btn2);
        snapshotButton2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                goHome();
            }
        });
        setCallback(canvas -> {
            if (poseResult != null) {
                for (Pose pose : poseResult.getPoses()) {
                    pose.draw(canvas);
                }
            }
            isComputing.set(false);
        });




    }
    public float[][][][] convert_yuv(Bitmap in){
        int batchNum = 0;
        float[][][][] out = new float[1][1800][1072][3];
        for (int x = 0; x < 2160; x++) {
            for (int y = 0; y < 1080; y++) {
                int pixel = in.getPixel(x, y);
                // Normalize channel values to [-1.0, 1.0]. This requirement varies by
                // model. For example, some models might require values to be normalized
                // to the range [0.0, 1.0] instead.
                out[batchNum][x][y][0] = (Color.red(pixel))/ 255.0f;
                out[batchNum][x][y][1] = (Color.green(pixel)) / 255.0f;
                out[batchNum][x][y][2] = (Color.blue(pixel))/ 255.0f;

            }
        }

        return out;
    }
    public float[][][][] call(float[][][][] input){
        float[][][][] output = new float[1][2160][1080][3];
        interpreter.getInterpreter().run(input, output);
        input = null; // gc
        return output;

    }

    @RequiresApi(api = Build.VERSION_CODES.P)
    @Override
    public void onImageAvailable(final ImageReader reader) {
        Image image = reader.acquireLatestImage();

        if (image == null) {
            return;
        }

        if (!shouldSample.get()) {
            image.close();
            return;
        }

        if (!isComputing.compareAndSet(false, true)) {
            image.close();
            return;
        }


        //visionImage = FritzVisionImage.fromMediaImage(image, orientation);
        //image.close();
      // input.order(ByteOrder.nativeOrder());
       // ByteBuffer output = ByteBuffer.allocateDirect(4* 1280 * 960*3);
       // output.order(ByteOrder.nativeOrder());
        // Analysis code for every frame
        // Preprocess the image
        visionImage = FritzVisionImage.fromMediaImage(image, orientation);
        runOnUiThread(new Runnable() {

            @Override
            public void run() {
                ImageView testImage = findViewById(R.id.testImage);
                Bitmap yuv_bitmap = visionImage.prepare(new Size(1072, 1800));
                Bitmap output = Bitmap.createBitmap(1072, 1800, Bitmap.Config.ARGB_8888);
                //interpreter.getInterpreter().run(yuv_bitmap, output);
                testImage.setImageBitmap(output);

            }
        });

       // Bitmap yuv = visionImage.buildSourceBitmap();


        //interpreter.run(in, out);
        requestRender();

        image.close();
    }

}
