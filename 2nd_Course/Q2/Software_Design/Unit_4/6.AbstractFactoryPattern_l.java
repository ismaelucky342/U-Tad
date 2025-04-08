// interface abstract factory 

interface Button {
    void render();
}

interface Window {
    void render();
}

class ButtonWindows implements Button {
    @Override
    public void render() {
        System.out.println("Rendering a Windows button.");
    }
}

class WindowWindows implements Window {
    @Override
    public void render() {
        System.out.println("Rendering a Windows window.");
    }
}

class ButtonMacOS implements Button {
    @Override
    public void render() {
        System.out.println("Rendering a macOS button.");
    }
}

class WindowMacOS implements Window {
    @Override
    public void render() {
        System.out.println("Rendering a macOS window.");
    }
}

interface factory {
    Button createButton();
    Window createWindow();
}

class factoryWindows {
    public Button createButton() {
        return new ButtonWindows();
    }

    public Window createWindow() {
        return new WindowWindows();
    }
}

class factoryMacOS {
    public Button createButton() {
        return new ButtonMacOS();
    }

    public Window createWindow() {
        return new WindowMacOS();
    }
}

// Main class to demonstrate the Abstract Factory Pattern
public class Main {
    public static void main(String[] args) {
        factoryWindows windowsFactory = new factoryWindows();
        Button windowsButton = windowsFactory.createButton();
        Window windowsWindow = windowsFactory.createWindow();
        windowsButton.render(); // Output: Rendering a Windows button.
        windowsWindow.render(); // Output: Rendering a Windows window.

        factoryMacOS macOSFactory = new factoryMacOS();
        Button macOSButton = macOSFactory.createButton();
        Window macOSWindow = macOSFactory.createWindow();
        macOSButton.render(); // Output: Rendering a macOS button.
        macOSWindow.render(); // Output: Rendering a macOS window.
    }
}