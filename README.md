# sony_demo_code

## Installation and Setup:
- Install Python (https://www.python.org/downloads/)

- Add the python installation path and script folder path in the environment variables

- Download node js (https://nodejs.org/en)

- Update the node js path in Environment variables path section (ex: In path: C:\Program Files\nodejs\ )

- Install appium using below command
  ```bash
      npm install appium -g

- pip install the appium python client
  ```bash
  pip install Appium-Python-Client

- Download the latest java JDK and update the path in the enviroment variable  (ex: JAVA_HOME: C:\Program Files\Java\jdk-17  &  In path: %JAVA_HOME%\bin )

- Download gradle and extract the zip file and move to local disk c  ( URL: https://gradle.org/install/ )

- Update the gradle path in new system variable (ex: Gradle_Home: C:\gradle-8.10.1  & In path: %Gradle_Home%\bin )

- Download Android studio from https://developer.android.com/studio and Install it.

- After the installation go to the installed folder (ex: C:\Users\ur_name\AppData\Local\Android\Sdk ) and validate three folders should present ("build-tools", "tools", "platform-tools")

- If tools folder missing, Open Android studio > settings > SDK manager > SDK tools > Uncheck the check box "Hide Obsolete packages" > Select "Andriod SDK tools (Obsolete)" > Install

- Set the android environment path. New system variable (ex: ANDROID_HOME: C:\Users\ur_name\AppData\Local\Android\Sdk  & In path add 3 path: %ANDROID_HOME%\build-tools   %ANDROID_HOME%\tools  %ANDROID_HOME%\platform-tools

- Download the  latest appium inspector "https://github.com/appium/appium-inspector/releases"

- Install appium ui automator 2 using below command
  ```bash
  appium driver install uiautomator2

- Check the appium server running using below command
  ```bash
  appium

- Create the virtual device in android studio and install the application
