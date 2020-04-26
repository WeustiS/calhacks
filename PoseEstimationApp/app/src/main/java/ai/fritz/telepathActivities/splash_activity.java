
	 
	/*
	 *	This content is generated from the API File Info.
	 *	(Alt+Shift+Ctrl+I).
	 *
	 *	@desc 		
	 *	@file 		splash
	 *	@date 		0
	 *	@title 		Splash
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

import java.util.Timer;
import java.util.TimerTask;

	public class splash_activity extends Activity {

	Timer timer;
	private View _bg__splash;
	private ImageView path_18;
	private View ellipse_3;
	private ImageView path_10;
	private ImageView path_11;
	private ImageView path_12;
	private ImageView path_13;
	private ImageView path_14;
	private ImageView path_15;
	private ImageView path_16;
	private ImageView path_17;
	private View ellipse_14;

	@Override
	public void onCreate(Bundle savedInstanceState) {

		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_splash);

		
		_bg__splash = (View) findViewById(R.id._bg__splash);
		path_18 = (ImageView) findViewById(R.id.path_18);
		ellipse_3 = (View) findViewById(R.id.ellipse_3);
		path_10 = (ImageView) findViewById(R.id.path_10);
		path_11 = (ImageView) findViewById(R.id.path_11);
		path_12 = (ImageView) findViewById(R.id.path_12);
		path_13 = (ImageView) findViewById(R.id.path_13);
		path_14 = (ImageView) findViewById(R.id.path_14);
		path_15 = (ImageView) findViewById(R.id.path_15);
		path_16 = (ImageView) findViewById(R.id.path_16);
		path_17 = (ImageView) findViewById(R.id.path_17);
		ellipse_14 = (View) findViewById(R.id.ellipse_14);
	
		timer = new Timer();
		timer.schedule(new TimerTask() {
			@Override
			public void run() {
				Intent intent = new Intent(splash_activity.this, home_activity.class);
				startActivity(intent);
				finish();
			}
		}, 2000);
		//custom code goes here
	
	}
}
	
	