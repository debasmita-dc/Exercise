package com.dp.adapter;

public class PaypalGateway {
    public void sendPaypalPayment(double amountInCents) {
        System.out.println("Processed " + amountInCents + " cents via PayPal");
    }
}
