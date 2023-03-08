import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketTimeoutException;

public class PingClient {
    private static final int requestNum = 10;
    private static final int timeOut = 1000;
    private static final String serverName = "127.0.0.1";
    private static final int serverPort = 2333;

    public static void main(String[] args) throws Exception {
        DatagramSocket clientSocket = new DatagramSocket();
        clientSocket.setSoTimeout(timeOut);
        for (int i = 0; i < requestNum; i++) {
            String message = "PING";
            byte[] buffer = message.getBytes();
            InetAddress serverAddress = InetAddress.getByName(serverName);
            DatagramPacket request = new DatagramPacket(buffer, buffer.length, serverAddress, serverPort);
            long startTime = System.currentTimeMillis();
            try {
                clientSocket.send(request);
                byte[] receiveBuffer = new byte[1024];
                DatagramPacket response = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                clientSocket.receive(response);
                String responseMessage = new String(response.getData(), 0, response.getLength());
                long RTT = (System.currentTimeMillis() - startTime) / 1000;
                System.out.println("Response from server: " + responseMessage + " RTT: " + RTT);
            } catch (SocketTimeoutException e) {
                long RTT = (System.currentTimeMillis() - startTime) / 1000;
                System.out.println("Packet lost, RTT: " + RTT);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        clientSocket.close();
    }
}
