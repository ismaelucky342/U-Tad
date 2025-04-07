# **Unit 2: Processes**

## **Overview**

This unit focuses on understanding processes in operating systems, their lifecycle, and management. It also introduces threads, explores scheduling algorithms, and includes hands-on exercises to solidify the concepts. By the end of this unit, students will have a thorough understanding of process management, thread utilization, and scheduling strategies.

---

## **Why Learn About Processes?**

### **Introduction**

Processes are the cornerstone of multitasking in modern operating systems. They represent the execution of programs and manage how system resources are utilized. Understanding processes is essential for efficient system-level programming and optimization.

### **Why Study Processes?**

- To understand how operating systems manage multiple tasks.
- To learn how processes are created, scheduled, and terminated.
- To explore threads as lightweight processes and their utility.
- To gain insights into scheduling algorithms that optimize system performance.

### **What Not to Expect from This Unit**

- Advanced deep dives into all possible process scheduling implementations.
- In-depth exploration of specific operating system internals beyond the core topics.

---

## **Processes**

### **Introduction**

This section introduces the fundamental concept of a process and its significance in operating systems.

### **What is a Process?**

A process is a program in execution, encompassing its code, data, and execution state. It serves as the primary entity for resource management in operating systems.

### **Process Map**

A process consists of the following components:

- **Code Segment:** The program's instructions.
- **Data Segment:** Variables and dynamic data.
- **Stack:** Function calls and control flow.
- **Heap:** Dynamically allocated memory.

---

## **Process Lifecycle**

### **Introduction**

The lifecycle of a process is a sequence of states that it undergoes during its existence.

### **Lifecycle Stages**

- **Process Creation:** Using system calls like `fork()` or `exec()`.
- **Process States:** New, ready, running, waiting, and terminated.
- **Process Activation:** Scheduling a process for execution.
- **Interruptions:** Handling events like I/O or signals.
- **Process Termination:** Cleaning up resources after completion.

### **Linux State Diagram**

A visual representation of the process states in Linux, illustrating transitions between states.

---

## **Threads**

### **Introduction**

Threads are lightweight processes that allow parallelism within a single process.

### **Concept and Utility**

- **What are Threads?** Threads share resources of a process but execute independently.
- **Advantages of Threads:** Faster context switching, resource sharing, and enhanced performance in multithreaded applications.

---

## **Scheduling**

### **Introduction**

Scheduling is the process of determining which process or thread gets CPU time.

### **Key Topics**

- **Process States Recap:** Contextualizing scheduling within process states.
- **KPIs for Scheduling:** Metrics like throughput, latency, and fairness.
- **Scheduling Algorithms:**
    - **FCFS:** Processes are executed in arrival order.
    - **Round Robin:** Time slices ensure fairness.
    - **Priority Scheduling:** Based on process priority levels.
    - **Linux Scheduler:** Explains how the Linux kernel schedules tasks.
    - **BSD Scheduler:** Insights into BSD system scheduling.
    - **xv6 Scheduler:** Overview of scheduling in xv6.
    - **Thread Scheduling:** Handling scheduling for threads.

---

## **Fork Exercises**

### **Introduction**

Explores process creation using `fork()`.

### **Exercises**

1. **Basic Usage:** Simple parent-child process creation.
2. **Parent vs Child:** Differentiating between parent and child processes.
3. **Multiple Processes:** Managing concurrent processes.
4. **Shared Resources:** Addressing shared memory challenges.
5. **Advanced Forking:** Complex scenarios for advanced process handling.

---

## **Scheduling Exercises**

### **Introduction**

Hands-on problems to implement and analyze scheduling algorithms.

### **Exercises**

1. **Custom Scheduler:** Implement and test a scheduling algorithm.
2. **Comparison Study:** Evaluate different scheduling strategies using practical examples.