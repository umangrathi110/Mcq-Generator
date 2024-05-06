# Deployment on Amazon EC2 Instance

## Steps

1. **Launch EC2 Instance**:
    - Launch an EC2 instance of type t2.small with 20 GB of memory.

2. **Update System**:
    ```bash
    sudo apt update
    ```

3. **Upgrade Packages**:
    ```bash
    sudo apt-get update
    sudo apt upgrade -y
    ```

4. **Install Required Packages**:
    ```bash
    sudo apt install git curl unzip tar make vim wget
    ```

5. **Clone the Repository**:
    Clone the repository to your EC2 instance:
    ```bash
    git clone https://github.com/umangrathi110/Mcq-Generator.git
    ```

6. **Create .env File**:
    Create a .env file to store the OpenAI API key in the cloned folder.

7. **Install pip**:
    ```bash
    sudo apt install python3-pip
    ```

8. **Install all the required packages**:
    ```bash
    sudo pip3 install -r requirements.txt
    ```

9. **Run the Streamlit Application**:
    Run the Streamlit application:
    ```bash
    python3 -m streamlit run streamlitapp.py
    ```

10. **Edit Security Group**:
    Edit the security group associated with your EC2 instance and open port 8501.

11. **Access the Application**:
    Access the Streamlit application by navigating to the public IP of your EC2 instance followed by port 8501 (e.g., http://<public_ip>:8501).

## Additional Notes

- Ensure that your EC2 instance has sufficient permissions and access to resources required by your application.
- Monitor the instance's resource usage to ensure optimal performance and scalability.





Deployment of the applicatio on the amazon ec2 instance 

steps 
1-> launch an ec2 instance of t2.small with 10 gb of memory 
2 -> sudo apt update
3 -> sudo apt-get update 
4-> sudo apt upgrade -g
5 -> sudo apt install git curl unzip tar make vim wget  

clone the repository 

create the .env for storing the openai_api_key 

install pip
sudo apt install python3-pip 

installing all the packages 
sudo install -r requirements.txt

run the streamlit application 
python3 -m streamlit run streamlitapp.py 

edit the security group and open the port 8501 and access the public ip of the instance with port 8501
