interface Engine {
    void turnOn();
}

interface Tires {
    void inflate();
}

interface Suspension {
    void adjust();
}

class RoadEngine implements Engine {
    @Override
    public void turnOn() {
        System.out.println("Road engine turned on.");
    }
}

class OffroadEngine implements Engine {
    @Override
    public void turnOn() {
        System.out.println("Offroad engine turned on.");
    }
}

class RoadTires implements Tires {
    @Override
    public void inflate() {
        System.out.println("Road tires inflated.");
    }
}

class OffroadTires implements Tires {
    @Override
    public void inflate() {
        System.out.println("Offroad tires inflated.");
    }
}

class RoadSuspension implements Suspension {
    @Override
    public void adjust() {
        System.out.println("Road suspension adjusted.");
    }
}

class OffroadSuspension implements Suspension {
    @Override
    public void adjust() {
        System.out.println("Offroad suspension adjusted.");
    }
}

interface Factory {
    Engine createEngine();
    Tires createTires();
    Suspension createSuspension();
}

class RoadFactory implements Factory {
    @Override
    public Engine createEngine() {
        return new RoadEngine();
    }

    @Override
    public Tires createTires() {
        return new RoadTires();
    }

    @Override
    public Suspension createSuspension() {
        return new RoadSuspension();
    }
}

class OffroadFactory implements Factory {
    @Override
    public Engine createEngine() {
        return new OffroadEngine();
    }

    @Override
    public Tires createTires() {
        return new OffroadTires();
    }

    @Override
    public Suspension createSuspension() {
        return new OffroadSuspension();
    }
}

// main

public class AbstractFactoryPattern {
    public static void main(String[] args) {
        Factory roadFactory = new RoadFactory();
        Engine roadEngine = roadFactory.createEngine();
        Tires roadTires = roadFactory.createTires();
        Suspension roadSuspension = roadFactory.createSuspension();

        roadEngine.turnOn();
        roadTires.inflate();
        roadSuspension.adjust();

        System.out.println("");

        Factory offroadFactory = new OffroadFactory();
        Engine offroadEngine = offroadFactory.createEngine();
        Tires offroadTires = offroadFactory.createTires();
        Suspension offroadSuspension = offroadFactory.createSuspension();

        offroadEngine.turnOn();
        offroadTires.inflate();
        offroadSuspension.adjust();
    }
}