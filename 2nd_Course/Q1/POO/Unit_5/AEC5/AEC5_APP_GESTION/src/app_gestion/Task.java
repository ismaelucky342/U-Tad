package app_gestion;

public class Task {
    private int id;
    private String name;
    private boolean isCompleted;

    public Task(int id, String name) {
        this.id = id;
        this.name = name;
        this.isCompleted = false;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public boolean isCompleted() {
        return isCompleted;
    }

    public void setCompleted(boolean isCompleted) {
        this.isCompleted = isCompleted;
    }

    @Override
    public String toString() {
        return (isCompleted ? "[Completada] " : "[Pendiente] ") + name;
    }
}
