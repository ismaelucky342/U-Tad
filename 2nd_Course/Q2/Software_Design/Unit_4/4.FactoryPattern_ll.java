//factory method

interface Button {
    void render();
}

class WindowsButton implements Button {
    @Override
    public void render() {
        System.out.println("Rendering a Windows button.");
    }
}

class MacOSButton implements Button {
    @Override
    public void render() {
        System.out.println("Rendering a macOS button.");
    }
}

class LinuxButton implements Button {
    @Override
    public void render() {
        System.out.println("Rendering a Linux button.");
    }
}

// Abstract factory class
abstract class Dialog {
    public void renderButton() {
        Button button = createButton();
        button.render();
    }

    protected abstract Button createButton();
}

// Concrete factory classes
class WindowsDialog extends Dialog {
    @Override
    protected Button createButton() {
        return new WindowsButton();
    }
}

class MacOSDialog extends Dialog {
    @Override
    protected Button createButton() {
        return new MacOSButton();
    }
}

class LinuxDialog extends Dialog {
    @Override
    protected Button createButton() {
        return new LinuxButton();
    }
}

// main
public class Main {
    public static void main(String[] args) {
        Dialog dialog = null;

        String os = System.getProperty("os.name").toLowerCase();
        if (os.contains("win")) {
            dialog = new WindowsDialog();
        } else if (os.contains("mac")) {
            dialog = new MacOSDialog();
        } else if (os.contains("nix") || os.contains("nux")) {
            dialog = new LinuxDialog();
        }

        if (dialog != null) {
            dialog.renderButton();
        } else {
            System.out.println("Unsupported operating system.");
        }
    }
}