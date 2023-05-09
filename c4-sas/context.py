from diagrams import Diagram
from diagrams.c4 import Person, Container, SystemBoundary, Relationship, System

graph_attr = {
    "splines": "spline",
}

with Diagram("Context View of Booking Management System", direction="TB", graph_attr=graph_attr):
    
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

    booking_system = Container(
        name="Booking Management System",
        technology="Java and Spring MVC",
        description="Provides the booking, hotel suppliers feeding and notification functionality.",
    )

    cost_center_tracking = System(
        name="Cost Center Traking System",
        description="System that manage the costs and payments of bookings",
        external=True,
    )

    employee >> Relationship("Review and Accepts Bookings") >> booking_system
    employee >> Relationship("Review and Update Business Trips") >> cost_center_tracking

    travel_manager >> Relationship("Manage Bookings/Transportations") >> booking_system
    travel_manager >> Relationship("Manage Configurations and Rules") >> booking_system
    travel_manager << Relationship("Alerts and Notifications") << booking_system
    travel_manager << Relationship("Creat Reports") << booking_system

    it_support >> Relationship("Technical Support") >> booking_system

    hotel_supplier >> Relationship("Upload Booking Details") >> booking_system
    transportation_supplier >> Relationship("Upload Transportation Details") >> booking_system

    cost_center_tracking >> Relationship("Hotels and Transport Requirements") >> booking_system