from diagrams import Diagram
from diagrams.c4 import Person, Container, SystemBoundary, Relationship, System

graph_attr = {
    "splines": "spline",
}

with Diagram("Container View of Booking Management System", direction="TB", graph_attr=graph_attr):
    
    with SystemBoundary("Internal Users"):
        employee = Person(
            name = "Employee", description="User that reviews and accept hotels and transportation"
        )

        travel_manager = Person(
            name = "Travel Manager", description="Manage and configure alerts and approve employee bookings"
        )

        it_support = Person(
            name = "IT Support", description="Keeps the system in good health and gives support to users"
        )

    with SystemBoundary("External Users"):
        hotel_supplier = Person(
            name = "Hotel Supplier", description="Upload bookings availability information"
        )

        transportation_supplier = Person(
            name = "Hotel Supplier", description="Upload transportation availability information"
        )

    with SystemBoundary("Booking Management System"):
        cost_center_adapter = Container(
            name="Cost Center Tracking Connector",
            technology="GraphQL/HTTPS",
            description="Provides the interaction between Cost Center and Booking System",
        )

        booking_ingest_api = Container(
            name="Booking Ingestion API",
            technology="JSON/HTTPS",
            description="Provides the API for booking ingestion",
        )

        transport_ingest_api = Container(
            name="Transportation Ingestion API",
            technology="JSON/HTTPS",
            description="Provides the API for transportation ingestion",
        )

        employee_web_app = Container(
            name="Employee Web Application",
            technology="Angular, NodeJS",
            description="Web application for User interaction",
        )

        manager_web_app = Container(
            name="Manager Web Application",
            technology="Angular, NodeJS",
            description="Web application for Manager and Support interaction",
        )

        notification_service = System(
            name="Email and Notification System",
            description="System that manage sends the notifications",
            external=True,
        )

        report_engine = System(
            name="Reporting Engine",
            description="BI Tool for reporting",
            external=False,
        )

    cost_center_tracking = System(
        name="Cost Center Traking System",
        description="System that manage the costs and payments of bookings",
        external=True,
    )


    employee >> Relationship("Review and Accepts Bookings") >> employee_web_app
    employee >> Relationship("Review and Update Business Trips") >> cost_center_tracking

    travel_manager >> Relationship("Manage Bookings/Transportations") >> manager_web_app
    travel_manager >> Relationship("Manage Configurations and Rules") >> manager_web_app
    travel_manager << Relationship("Alerts and Notifications") << notification_service
    travel_manager << Relationship("Create Reports") << report_engine

    it_support >> Relationship("Technical Support") >> manager_web_app

    hotel_supplier >> Relationship("Upload Booking Details") >> booking_ingest_api
    transportation_supplier >> Relationship("Upload Transportation Details") >> transport_ingest_api

    cost_center_tracking >> Relationship("Hotels and Transport Requirements") >> cost_center_adapter