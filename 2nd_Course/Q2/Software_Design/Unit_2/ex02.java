package com.utad.inso.diso.strategy.area;

public interface AreaStrategy {

    public Double calculaArea(Double parametro);

}

public class CircleAreaStrategy implements AreaStrategy {

    public Double calculaArea(Double parametro) {

        return Math.PI * Math.pow(parametro, 2);

    }

}

public class SquareAreaStrategy implements AreaStrategy {

    public Double calculaArea(Double parametro) {

        return Math.pow(parametro, 2);

    }

}

public class ContextAreaStrategy {

    //1. Interface común como componente privado
    private AreaStrategy areaStrategy;

    //2. La estrategia debe establecerse como parámetro de constructor
    public ContextAreaStrategy(AreaStrategy areaStrategy) {

        super();

        this.areaStrategy = areaStrategy;

    }

    public AreaStrategy getAreaStrategy() {

        return areaStrategy;

    }

    //3. La estrategia debe ser intercambiable
    public void setAreaStrategy(AreaStrategy areaStrategy) {

        this.areaStrategy = areaStrategy;

    }

    public Double calculaArea(Double parametro) {

        //4. Delegación por composición (agregación)
        return this.areaStrategy.calculaArea(parametro);

    }

}
