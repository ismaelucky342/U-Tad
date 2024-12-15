package app_gestion;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JList;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

public class TaskApp {
    private JFrame frame;
    private JTextField taskInput;
    private DefaultListModel<Task> taskListModel;
    private JList<Task> taskList;
    private JLabel statsLabel;
    private TaskManager taskManager;

    public TaskApp() {
        taskManager = new TaskManager();
        initialize();
    }

    private void initialize() {
        // Configuración del marco principal
        frame = new JFrame("Gestor de Tareas");
        frame.setSize(500, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        // Menú
        JMenuBar menuBar = new JMenuBar();
        JMenu fileMenu = new JMenu("Archivo");
        JMenuItem newMenuItem = new JMenuItem("Nuevo");
        JMenuItem exitMenuItem = new JMenuItem("Salir");
        fileMenu.add(newMenuItem);
        fileMenu.add(exitMenuItem);

        JMenu helpMenu = new JMenu("Ayuda");
        JMenuItem aboutMenuItem = new JMenuItem("Acerca de");
        helpMenu.add(aboutMenuItem);

        menuBar.add(fileMenu);
        menuBar.add(helpMenu);
        frame.setJMenuBar(menuBar);

        // Panel superior: Entrada y botón de agregar
        JPanel topPanel = new JPanel();
        topPanel.setLayout(new BorderLayout());
        taskInput = new JTextField();
        JButton addButton = new JButton("Agregar");
        topPanel.add(taskInput, BorderLayout.CENTER);
        topPanel.add(addButton, BorderLayout.EAST);

        // Lista de tareas
        taskListModel = new DefaultListModel<>();
        taskList = new JList<>(taskListModel);
        JScrollPane taskScrollPane = new JScrollPane(taskList);

        // Panel inferior: Botones de acción y estadísticas
        JPanel bottomPanel = new JPanel();
        bottomPanel.setLayout(new GridLayout(2, 1));
        JPanel buttonPanel = new JPanel();
        JButton completeButton = new JButton("Marcar como Completada");
        JButton deleteButton = new JButton("Eliminar");
        buttonPanel.add(completeButton);
        buttonPanel.add(deleteButton);

        statsLabel = new JLabel("Tareas: 0, Completadas: 0, Pendientes: 0");
        bottomPanel.add(buttonPanel);
        bottomPanel.add(statsLabel);

        // Añadir componentes al marco principal
        frame.add(topPanel, BorderLayout.NORTH);
        frame.add(taskScrollPane, BorderLayout.CENTER);
        frame.add(bottomPanel, BorderLayout.SOUTH);

        // Acciones del menú
        newMenuItem.addActionListener(e -> resetApp());
        exitMenuItem.addActionListener(e -> System.exit(0));
        aboutMenuItem.addActionListener(e -> JOptionPane.showMessageDialog(frame, "Gestor de Tareas v1.0\nDesarrollado en Java", "Acerca de", JOptionPane.INFORMATION_MESSAGE));

        // Acciones de los botones
        addButton.addActionListener(e -> addTask());
        completeButton.addActionListener(e -> markTaskCompleted());
        deleteButton.addActionListener(e -> deleteTask());

        // Mostrar el marco
        frame.setVisible(true);
    }

    private void addTask() {
        String taskName = taskInput.getText().trim();
        if (!taskName.isEmpty()) {
            taskManager.addTask(taskName);
            taskInput.setText("");
            refreshTaskList();
        } else {
            JOptionPane.showMessageDialog(frame, "El nombre de la tarea no puede estar vacío.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void markTaskCompleted() {
        Task selectedTask = taskList.getSelectedValue();
        if (selectedTask != null) {
            taskManager.markTaskCompleted(selectedTask.getId());
            refreshTaskList();
        } else {
            JOptionPane.showMessageDialog(frame, "Seleccione una tarea para marcar como completada.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void deleteTask() {
        Task selectedTask = taskList.getSelectedValue();
        if (selectedTask != null) {
            taskManager.removeTask(selectedTask.getId());
            refreshTaskList();
        } else {
            JOptionPane.showMessageDialog(frame, "Seleccione una tarea para eliminar.", "Error", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void refreshTaskList() {
        taskListModel.clear();
        for (Task task : taskManager.getTasks()) {
            taskListModel.addElement(task);
        }
        statsLabel.setText(String.format("Tareas: %d, Completadas: %d, Pendientes: %d",
                taskManager.getTotalTasks(), taskManager.getCompletedTasks(), taskManager.getPendingTasks()));
    }

    private void resetApp() {
        taskManager = new TaskManager();
        refreshTaskList();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(TaskApp::new);
    }
}

