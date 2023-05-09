from diagrams import Diagram
from diagrams.c4 import Person, Container, SystemBoundary, Relationship, System, Database

graph_attr = {
    "splines": "spline",
}

with Diagram("Component View of Booking Management System", direction="TB", graph_attr=graph_attr):
    
    with SystemBoundary("Internal Users"):
        travel_manager = Person(
            name = "Travel Manager", description="Manage and configure alerts and approve employee bookings"
        )

    with SystemBoundary("Booking Management System"):

        manager_web_app = Container(
            name="Manager Web Application",
            technology="Angular, NodeJS",
            description="Web application for Manager and Support interaction",
        )

        booking_manager_api = Container(
            name="Manager API",
            technology="JSON/HTTPS",
            description="API for Manager",
        )

        database = Database(
            name="Rules DB",
            technology="DynamoDB",
            description="Stores Rules Details"
        )

        report_database = Database(
            name="Reporting DB",
            technology="AuroraDB",
            description="Stores Report Details"
        )

        report_engine = System(
            name="Reporting Engine",
            description="BI Tool for reporting",
            external=False,
        )

        sso_security = System(
            name="SSO",
            description="SSO System for Security",
            external=False,
        )

        with SystemBoundary("Booking Management System"):
            
            sns = System(
                name="Email and Notification System",
                description="System that manage sends the notifications",
                external=True,
            )

            sqs = System(
                name="Event Delivery System",
                description="System that manage sends the notifications",
                external=True,
            )

    travel_manager >> Relationship("Interacts") >> manager_web_app
    manager_web_app >> Relationship("Requests") >> booking_manager_api
    booking_manager_api >> Relationship("Authenticate and Authorize User") >> sso_security
    booking_manager_api << Relationship("Grants or Reject Auth") << sso_security
    booking_manager_api >> Relationship("CRUD for Rules") >> database
    booking_manager_api >> Relationship("Send Event Notification") >> sqs
    booking_manager_api >> Relationship("Subscribe Users") >> sns
    sqs >> Relationship("Emit event to subcribers") >> sns
    travel_manager << Relationship("Email Alerts and Notifications") << sns
    booking_manager_api << Relationship("Reports") << report_engine
    report_engine >> Relationship("CRUD for Reporting") >> report_database
