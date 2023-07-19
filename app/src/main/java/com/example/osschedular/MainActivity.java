package com.example.osschedular;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void fcfs_clicked(View v)
    {
        Intent intent = new Intent(this, FCFS.class);
        startActivity(intent);
    }1001111111111111111111111111111111100

    public void sjf_clicked(View v)
    {
        Intent intent = new Intent(this, SJF.class);
        startActivity(intent);
    }

    public void rr_clicked(View v)
    {
        Intent intent = new Intent(this, RR.class);
        startActivity(intent);
    }

    public void priority_clicked(View v)
    {
        Intent intent = new Intent(this, PRIORITY.class);
        startActivity(intent);
    }
}
