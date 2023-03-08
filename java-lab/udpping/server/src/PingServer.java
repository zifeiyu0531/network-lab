import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.InputStreamReader;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Random;

public class PingServer {
    private static final double LOSS_RATE = 0.3;
    private static final int AVERAGE_DELAY = 100;
    private static final int port = 2333;

    public static void main(String[] args) throws Exception {
        Random random = new Random();
        DatagramSocket socket = new DatagramSocket(port);
        System.out.println("Server start to listen.");

        while (true) {
            DatagramPacket request = new DatagramPacket(new byte[1024], 1024);
            socket.receive(request);

            if (random.nextDouble() < LOSS_RATE) {
                System.out.println("packet lost");
                continue;
            }

            printData(request);

            Thread.sleep((long)(random.nextDouble() * 2 * AVERAGE_DELAY));

            InetAddress clientHost = request.getAddress();
            int clientPort = request.getPort();
            byte[] buf = "PONG".getBytes();
            DatagramPacket reply = new DatagramPacket(buf, buf.length, clientHost, clientPort);
            socket.send(reply);
        }
    }

    private static void printData(DatagramPacket request) throws Exception {
        byte[] buf = request.getData();
        ByteArrayInputStream bais = new ByteArrayInputStream(buf);
        InputStreamReader isr = new InputStreamReader(bais);
        BufferedReader br = new BufferedReader(isr);

        String line = br.readLine();
        System.out.println("Received from " + request.getAddress().getHostAddress() + ":" + line);
    }
}
