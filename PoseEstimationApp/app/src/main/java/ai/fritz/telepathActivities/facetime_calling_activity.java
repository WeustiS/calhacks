
	 
	/*
	 *	This content is generated from the API File Info.
	 *	(Alt+Shift+Ctrl+I).
	 *
	 *	@desc 		
	 *	@file 		facetime_calling
	 *	@date 		0
	 *	@title 		Facetime_calling
	 *	@author 	
	 *	@keywords 	
	 *	@generator 	Export Kit v1.2.9.xd
	 *
	 */
	

package ai.fritz.telepathActivities;

    import android.app.Activity;
    import android.content.Intent;
    import android.os.Bundle;
    import android.view.View;
    import android.widget.ImageView;
    import android.widget.TextView;



    public class facetime_calling_activity extends Activity {


        private View _bg__facetime_calling;
        private View ellipse_1;
        private ImageView _0;
        private TextView dr__eustis;
        private TextView calling_;
        private ImageView polygon_1;
        private TextView home;
        private View ellipse_2;
        private ImageView icon_awesome_phone_slash;

        @Override
        public void onCreate(Bundle savedInstanceState) {

            super.onCreate(savedInstanceState);
            setContentView(R.layout.facetime_calling);


            _bg__facetime_calling = (View) findViewById(R.id._bg__facetime_calling);
            ellipse_1 = (View) findViewById(R.id.ellipse_1);
            _0 = (ImageView) findViewById(R.id._0);
            dr__eustis = (TextView) findViewById(R.id.dr__eustis);
            calling_ = (TextView) findViewById(R.id.calling_);
            //polygon_1 = (ImageView) findViewById(R.id.polygon_1);
            home = (TextView) findViewById(R.id.home);
            ellipse_2 = (View) findViewById(R.id.ellipse_2);
            icon_awesome_phone_slash = (ImageView) findViewById(R.id.icon_awesome_phone_slash);


            //custom code goes here

        }
        public void goHome() {
            Intent intent = new Intent(this, home_activity.class);
            startActivity(intent);
        }
    }

	
	