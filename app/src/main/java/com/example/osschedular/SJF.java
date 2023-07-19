package com.example.osschedular;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class SJF extends AppCompatActivity {

    TextView at_answer;
    TextView bt_answer;
    TextView ct_answer;
    TextView tat_answer;
    TextView wt_answer;
    TextView rt_answer;

    EditText nop;
    EditText at;
    EditText bt;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_sjf);

        at_answer = (TextView)findViewById(R.id.at_answer);
        bt_answer = (TextView)findViewById(R.id.bt_answer);
        ct_answer = (TextView)findViewById(R.id.ct_answer);
        tat_answer = (TextView)findViewById(R.id.tat_answer);
        wt_answer = (TextView)findViewById(R.id.wt_answer);
        rt_answer = (TextView)findViewById(R.id.rt_answer);


        nop = (EditText)findViewById((R.id.nop));
        at = (EditText)findViewById((R.id.at));
        bt = (EditText)findViewById((R.id.bt));
    }
    public void click(View v)
    {
        String n = nop.getText().toString().trim();
        String a = at.getText().toString().trim();
        String b = bt.getText().toString().trim();

        if(n.matches("[0-9]+") && n.length()>0)
        {
            String test_a = a;
            String test_b = b;

            int n1 = Integer.parseInt(n);
            if(n1 > 10)
            {
                Toast.makeText(SJF.this, "Number Of Process is greater than 10", Toast.LENGTH_SHORT).show();
            }
            else
            {
                String[] temp1 = test_a.split(" ");
                String[] temp2 = test_b.split(" ");

                test_a = test_a.replaceAll(" ", "");
                test_b = test_b.replaceAll(" ", "");

                if(test_a.matches("[0-9]+") && temp1.length==n1)
                {
                    if(test_b.matches("[0-9]+") && temp2.length==n1)
                    {
                        String s = a+" "+b;

                        String[] str = null;
                        str = s.split(" ");

                        if (! Python.isStarted()) {
                            Python.start(new AndroidPlatform(this));
                        }

                        Python py = Python.getInstance();
                        PyObject pyobj = py.getModule("SJF");

                        PyObject pyObject = pyobj.callAttr("algorithm",n, str);

                        String answer = pyObject.toString();
                        String[] ans = answer.split(" ");

                        at_answer.setText(ans[0]);
                        bt_answer.setText(ans[1]);
                        ct_answer.setText(ans[2]);
                        tat_answer.setText(ans[3]);
                        wt_answer.setText(ans[4]);
                        rt_answer.setText(ans[5]);

                    }
                    else
                    {
                        Toast.makeText(SJF.this, "invalid input", Toast.LENGTH_SHORT).show();
                    }
                }
                else
                {
                    Toast.makeText(SJF.this, "invalid input", Toast.LENGTH_SHORT).show();
                }
            }

        }
        else
        {
            Toast.makeText(SJF.this, "invalid input", Toast.LENGTH_SHORT).show();
        }
    }
}