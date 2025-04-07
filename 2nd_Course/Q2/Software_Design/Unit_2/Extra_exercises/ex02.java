package com.utad.inso.diso.strategy.area;

// Interface for area calculation strategies
public interface AreaStrategy {
    Double calculaArea(Double parametro);
}

// Strategy for calculating the area of a circle
public class CircleAreaStrategy implements AreaStrategy {
    @Override
    public Double calculaArea(Double parametro) {
        return Math.PI * Math.pow(parametro, 2);
    }
}

// Strategy for calculating the area of a square
public class SquareAreaStrategy implements AreaStrategy {
    @Override
    public Double calculaArea(Double parametro) {
        return Math.pow(parametro, 2);
    }
}

// Context class to use different area calculation strategies
public class ContextAreaStrategy {

    // Interface as a private component
    private AreaStrategy areaStrategy;

    // Constructor to set the strategy
    public ContextAreaStrategy(AreaStrategy areaStrategy) {
        this.areaStrategy = areaStrategy;
    }

    // Getter for the strategy
    public AreaStrategy getAreaStrategy() {
        return areaStrategy;
    }

    // Setter to allow strategy swapping
    public void setAreaStrategy(AreaStrategy areaStrategy) {
        this.areaStrategy = areaStrategy;
    }

    // Delegation to the strategy for area calculation
    public Double calculaArea(Double parametro) {
        return areaStrategy.calculaArea(parametro);
    }
}
