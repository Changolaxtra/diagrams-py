from diagrams import Diagram
from diagrams.aws.database import Aurora
from diagrams.aws.compute import EKS
from diagrams.aws.network import CF
from diagrams.aws.security import Cognito, IAM
from diagrams.aws.storage import S3
from diagrams.aws.integration import SQS, SNS
from diagrams.aws.general import Users, User, TraditionalServer
from diagrams.aws.network import APIGateway

graph_attr = {
    "splines": "spline",
}

with Diagram("Deployment View of Booking Management System", direction="LR"):
    
    users = Users("EPAM Users")
    users_api =  APIGateway("Users API")
    sso = Cognito("SSO : Authentication")
    cdn = CF("Cache Static Resources")

    static = S3("Static Resources")

    k8s = EKS("Booking System")
    database =  Aurora("System DB")

    suppliers_api = APIGateway("Suppliers API")
    transport_supplier = User("Transport Supplier")
    hotel_supplier = User("Hotel Supplier")
    suppliers_auth = IAM("Suppliers Authentication")

    cost_center = TraditionalServer("Cost Center")
    hotel_search_service = TraditionalServer("Hotel Search Service")
    transport_search_service = TraditionalServer("Transport Search Service")
    sqs = SQS("Notification Queue")
    sns = SNS("Notification Delivery")
    

   
    users >> users_api
    users_api >> sso
    users_api >> cdn
    cdn >> static
    users_api >> k8s
    
    k8s >> database
    k8s >> cost_center
    k8s >> hotel_search_service
    k8s >> transport_search_service
    k8s >> sns
    sns >> sqs
    sqs >> users

    hotel_supplier >> suppliers_api
    transport_supplier >> suppliers_api
    suppliers_api >> k8s
    suppliers_api >> suppliers_auth
    suppliers_api >> cdn



    
    

