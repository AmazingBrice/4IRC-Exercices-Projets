package cpe.iot.madmomoiquipue;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class MainActivity extends AppCompatActivity {

    private Button btn;
    private TextView txt;
    private InetAddress address ;
    private int PORT;
    private DatagramSocket UDPSocket;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btn = findViewById(R.id.button2);
        txt = findViewById(R.id.lblx);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                txt.setText("Plop");
                sendMsg("Plop");
            }
        });

        try{
            UDPSocket = new DatagramSocket();
            PORT = 8081;
            address = InetAddress.getByName("10.150.0.39");

        }catch (Exception e){
            Log.e("Crash","Dans le onCreate");
        }

    }

    public void sendMsg(final String s) {
        (new Thread(){
            @Override
            public void run() {
                try{
                    byte[] data = s.getBytes();
                    DatagramPacket packet = new DatagramPacket(data, data.length, address, PORT);
                    UDPSocket.send(packet);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }).start();
    }
}






