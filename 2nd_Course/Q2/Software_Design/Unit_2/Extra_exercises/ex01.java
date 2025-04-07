package com.utad.inso.diso.strategy;

public interface TextFormatterStrategy {  //superclase común

    public void format(String text);

}

//Estrategia concreta (se usa como estrategia por defecto)
public class EchoTextFormatter implements TextFormatterStrategy {

    public void format(String text) {

        System.out.println("[EchoTextFormatter]: " + text);

    }

}

//Estrategia concreta
public class CamelTextFormatter implements TextFormatterStrategy {

    public void format(String text) {

        StringBuilder camelText = new StringBuilder("");

        for (int i = 0; i < text.length(); i++) {

            if (i % 2 == 0) {

                camelText.append(Character.toUpperCase(text.charAt(i)));

            } else {
                camelText.append(Character.toLowerCase(text.charAt(i)));

            }

        }

        System.out.println(



    "[CamelTextFormatter]:

 " +camelText.toString()); 

      }

}

//Contexto

public class TextEditorContext {

    //Relación de composición (agregación)    
    private TextFormatterStrategy textFormatterStrategy;

    public TextEditorContext() {

        this(new EchoTextFormatter());

    }

    public TextEditorContext(
            TextFormatterStrategy textFormatterStrategy) {

        super();

        this.textFormatterStrategy = textFormatterStrategy;

    }

    public TextFormatterStrategy getTextFormatterStrategy() {

        return textFormatterStrategy;

    }

    public void setTextFormatterStrategy( //Permite la intercambiabilidad

            TextFormatterStrategy textFormatterStrategy) {

        this.textFormatterStrategy = textFormatterStrategy;

    }

    public void format(String text) {

        //Delegación por composición agregación
        this.textFormatterStrategy.format(text);

    }

}

public class EditorStrategyPatternTest {

    public static void main(String[] args) {

        TextFormatterStrategy capTextformatterStrategy
                = new CapTextFormatter();

        TextFormatterStrategy lowerTextFormatterStrategy
                = new LowerTextFormatter();

//TODO Realiza los cambios para que se aplique por defecto la estrategia Echo
        TextEditorContext editor = new TextEditorContext();

//TextEditorContext editor = new TextEditorContext(capTextformatterStrategy); 
        editor.format("Wellcome to this Strategy editor");

        //Aplica estrategia
        editor.setTextFormatterStrategy(capTextformatterStrategy);

        editor.format("Testing text in caps formatter");

        //Aplica estrategia
        editor.setTextFormatterStrategy(lowerTextFormatterStrategy);

        editor.format("Testing text in lower formatter");

        //TODO Realiza el cambio para aplicar la estrategia CamelText
        editor.setTextFormatterStrategy(new CamelTextFormatter());

        editor.format("Testing text in camel formatter");

    }

}



package com.utad.diso.unidad2.strategy;

public interface TextFormatterStrategy {

    public void format(String text);

}

public class LowerTextFormatter implements TextFormatterStrategy {

    public void format(String text) {

        System.out.println("[LowerTextFormatter]: " + text.toLowerCase());

    }

}

public class CapTextFormatter implements TextFormatterStrategy {

    public void format(String text) {

        System.out.println("[CapTextFormatter]: " + text.toUpperCase());

    }

}
