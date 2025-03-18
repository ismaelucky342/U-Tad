package ex00;

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
    TextFormatterStrategy capTextformatterStrategy =
new CapTextFormatter();
    TextFormatterStrategy lowerTextFormatterStrategy =
new LowerTextFormatter();    
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