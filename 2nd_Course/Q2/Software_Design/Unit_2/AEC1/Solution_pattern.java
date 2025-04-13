// Context Class
public class KinderGardenServiceContext {
    private DoctorServiceStrategy serviceStrategy;

    public KinderGardenServiceContext(DoctorServiceStrategy serviceStrategy) {
        this.serviceStrategy = serviceStrategy;
    }

    public void setServiceStrategy(DoctorServiceStrategy serviceStrategy) {
        this.serviceStrategy = serviceStrategy;
    }

    public void applyServiceStrategy() {
        serviceStrategy.inspectChildren();
        serviceStrategy.sendResultsInspection();
        serviceStrategy.sendInvoice();
    }
}

// Abstract Class - Medical Service Strategy
abstract class DoctorServiceStrategy {
    public void applyServiceStrategy() {
        inspectChildren();
        sendResultsInspection();
        sendInvoice();
    }

    protected abstract void inspectChildren();

    public void sendResultsInspection() {
        System.out.println("Inspection results have been sent");
    }

    public void sendInvoice() {
        System.out.println("The invoice for the service has been sent");
    }
}

// Fong Strategy
class FongDoctorStrategy extends DoctorServiceStrategy {
    @Override
    protected void inspectChildren() {
        System.out.println("FongDoctorStrategy: I am inspecting the children");
        System.out.println("Inspection task completed");
    }
}

// Wang Strategy
class WangDoctorStrategy extends DoctorServiceStrategy {
    @Override
    protected void inspectChildren() {
        System.out.println("WangDoctorStrategy: I am inspecting the children");
        System.out.println("Inspection task completed");
    }
}

// Main Class to test
public class TestKinderGardenService {
    public static void main(String[] args) {
        // Assuming Dr. Fong is consulting
        KinderGardenServiceContext kinderGardenContext = new KinderGardenServiceContext(new FongDoctorStrategy());
        kinderGardenContext.applyServiceStrategy();

        // Changing the medical service, now Dr. Wang is consulting
        kinderGardenContext.setServiceStrategy(new WangDoctorStrategy());
        kinderGardenContext.applyServiceStrategy();
    }
}