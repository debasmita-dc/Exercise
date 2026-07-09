package com.dp.command;

public class Main {
    public static void main(String[] args) {
        Light livingRoomLight = new Light("Living Room");
        RemoteControl remote = new RemoteControl();

        remote.setCommand(new LightOnCommand(livingRoomLight));
        remote.pressButton();

        remote.setCommand(new LightOffCommand(livingRoomLight));
        remote.pressButton();
    }
}
