package com.dp.proxy;

public class RealImage implements Image {
    private final String fileName;

    public RealImage(String fileName) {
        this.fileName = fileName;
        loadFromServer();
    }

    private void loadFromServer() {
        System.out.println("Loading " + fileName + " from remote server");
    }

    @Override
    public void display() {
        System.out.println("Displaying " + fileName);
    }
}
