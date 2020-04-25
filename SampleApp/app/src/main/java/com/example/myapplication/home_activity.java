
	 
	/*
	 *	This content is generated from the API File Info.
	 *	(Alt+Shift+Ctrl+I).
	 *
	 *	@desc 		
	 *	@file 		home
	 *	@date 		0
	 *	@title 		Home
	 *	@author 	
	 *	@keywords 	
	 *	@generator 	Export Kit v1.2.9.xd
	 *
	 */
	

package com.example.myapplication;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;


import android.view.View;
import android.widget.ImageButton;
import android.widget.ScrollView;
import android.widget.TextView;
import android.widget.ImageView;

public class home_activity extends Activity {

	
	private View _bg__home;
	private View rectangle_11;
	private TextView hello_illini__how_are_you_today_;
	private TextView upcoming_call;
	private TextView call_a_doctor_now;
	private View rectangle_1;
	private ImageButton call_doctor;
	private TextView march_2__11_30_am;
	private TextView this_saturday;
	private ImageView path_1;
	private ImageView path_2;
	private View rectangle_8;
	private View rectangle_10;
	private View ellipse_1;
	private ImageView _0;
	private View ellipse_1_ek1;
	private TextView william_eustis;
	private TextView psychicatrist_at_carle;
	private ImageView path_3;
	private ImageView path_4;
	private TextView make_a_call;
	private TextView facetime_with_currently_available_doctors;
	private ImageView polygon_1;
	private ImageView icon_ionic_md_home;
	private ScrollView home;
	private ImageView icon_awesome_history;
	private TextView history;
	private ImageView path_5;
	private ImageView path_6;
	private ImageView path_7;
	private TextView schedule;
	private ImageView path_8;
	private ImageView path_9;
	private TextView chat;
	private ImageView icon_material_person;
	private TextView profile;

	@Override
	public void onCreate(Bundle savedInstanceState) {

		super.onCreate(savedInstanceState);
		setContentView(R.layout.home);

		
		_bg__home = (View) findViewById(R.id._bg__home);
		rectangle_11 = (View) findViewById(R.id.rectangle_11);
		hello_illini__how_are_you_today_ = (TextView) findViewById(R.id.hello_illini__how_are_you_today_);
		upcoming_call = (TextView) findViewById(R.id.upcoming_call);
		call_a_doctor_now = (TextView) findViewById(R.id.call_a_doctor_now);
		rectangle_1 = (View) findViewById(R.id.rectangle_1);

		call_doctor =  (ImageButton) findViewById(R.id.call_doctor); // Call a doctor button

		march_2__11_30_am = (TextView) findViewById(R.id.march_2__11_30_am);
		this_saturday = (TextView) findViewById(R.id.this_saturday);
		path_1 = (ImageView) findViewById(R.id.path_1);
		path_2 = (ImageView) findViewById(R.id.path_2);
		rectangle_8 = (View) findViewById(R.id.rectangle_8);
		rectangle_10 = (View) findViewById(R.id.rectangle_10);
		ellipse_1 = (View) findViewById(R.id.ellipse_1);
		_0 = (ImageView) findViewById(R.id._0);
		ellipse_1_ek1 = (View) findViewById(R.id.ellipse_1_ek1);
		william_eustis = (TextView) findViewById(R.id.william_eustis);
		psychicatrist_at_carle = (TextView) findViewById(R.id.psychicatrist_at_carle);
		path_3 = (ImageView) findViewById(R.id.path_3);
		path_4 = (ImageView) findViewById(R.id.path_4);
		make_a_call = (TextView) findViewById(R.id.make_a_call);
		facetime_with_currently_available_doctors = (TextView) findViewById(R.id.facetime_with_currently_available_doctors);
		//polygon_1 = (ImageView) findViewById(R.id.polygon_1);
		icon_ionic_md_home = (ImageView) findViewById(R.id.icon_ionic_md_home);
		home = (ScrollView) findViewById(R.id.home);
		icon_awesome_history = (ImageView) findViewById(R.id.icon_awesome_history);
		//history = (TextView) findViewById(R.id.history);
		path_5 = (ImageView) findViewById(R.id.path_5);
		path_6 = (ImageView) findViewById(R.id.path_6);
		path_7 = (ImageView) findViewById(R.id.path_7);
		//schedule = (TextView) findViewById(R.id.schedule);
		path_8 = (ImageView) findViewById(R.id.path_8);
		path_9 = (ImageView) findViewById(R.id.path_9);
		//chat = (TextView) findViewById(R.id.chat);
		icon_material_person = (ImageView) findViewById(R.id.icon_material_person);
		//profile = (TextView) findViewById(R.id.profile);


		//custom code goes here

		call_doctor.setOnClickListener(new View.OnClickListener() {
			@Override
			public void onClick(View v) {
				makeCall();
			}
		});


	}

	public void makeCall() {
		Intent intent = new Intent (this, facetime_calling_activity.class);
		startActivity (intent);

	}
}
	
	