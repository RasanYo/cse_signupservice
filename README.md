<p align="center">
<img src="src/frontend/static/icons/Hipster_HeroLogoMaroon.svg" width="300" alt="Online Boutique" />
</p>

This is an extended version of the google online boutique with an additional sign-up microservice written in Python using the Flask library for the UI, the Firebase authentication library.
For monitoring purposes it uses InfluxDB visualized on a Grafana dashboard that can be accessed here :
https://rasanhy.grafana.net/dashboard/snapshot/zX57EPkHie9i1OojeJBFiA3WbM7EqcLx

To try out the application yourself, clone the repository on your computer with 
```
git clone https://github.com/RasanYo/cse_signupservice.git
```

To test the signup feature locally, use the following instructions:
```
cd src/signupservice
pip install -r requirements.txt
cd src
py app.py
```
If the launch is successful, you should see in the command prompt the local address under which the app is running


To deploy the whole cluster, do the following:

1.
```
PROJECT_ID="<your-project-id>"
gcloud services enable container.googleapis.com --project ${PROJECT_ID}
```

2.
```
REGION=us-central1
gcloud container clusters create-auto onlineboutique \
    --project=${PROJECT_ID} --region=${REGION}
```

3.
```
ZONE=us-central1-b
gcloud container clusters create onlineboutique \
    --project=${PROJECT_ID} --zone=${ZONE} \
    --machine-type=e2-standard-2 --num-nodes=4
```

4.
```
kubectl apply -f ./release/kubernetes-manifests.yaml
```

5.
```
kubectl get pods
```

Once all the pods are running, do:

6.
```
kubectl get svc
```

You should see:
```
NAME                     TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)          
adservice                ClusterIP      10.108.6.73     <none>           9555/TCP         
cartservice              ClusterIP      10.108.3.162    <none>           7070/TCP         
checkoutservice          ClusterIP      10.108.5.90     <none>           5050/TCP         
currencyservice          ClusterIP      10.108.0.92     <none>           7000/TCP         
emailservice             ClusterIP      10.108.5.227    <none>           5000/TCP         
frontend                 ClusterIP      10.108.4.209    <none>           80/TCP           
frontend-external        LoadBalancer   10.108.14.172   34.172.177.142   80:31541/TCP     
kubernetes               ClusterIP      10.108.0.1      <none>           443/TCP          
paymentservice           ClusterIP      10.108.4.187    <none>           50051/TCP        
productcatalogservice    ClusterIP      10.108.2.135    <none>           3550/TCP         
recommendationservice    ClusterIP      10.108.14.12    <none>           8080/TCP         
redis-cart               ClusterIP      10.108.13.197   <none>           6379/TCP         
shippingservice          ClusterIP      10.108.14.124   <none>           50051/TCP        
signupservice            ClusterIP      10.108.4.151    <none>           3000/TCP         
signupservice-external   LoadBalancer   10.108.0.181    34.171.32.106    3000:30022/TCP   
```

With the external ip address of signupservice-external, enter in your the search bar of your browser <EXTERNAL_IP>:3000 to access the signup page.
Once there you can enter the email address and the password with which you want to login.


Made by Jonathan Zöllinger, Pascal Schütze and Rasan Younis
(Originally we had a different repository consisting just of the folder we were working in. Here is the link https://github.com/RasanYo/signupservice.git. At the end we created a new repository with all the other files. So it might seem as if only one person did all the commits for this repository, but in reality everyone contributed equally.)

