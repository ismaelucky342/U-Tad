#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <pthread.h>
#include <sys/time.h>
#include <semaphore.h>
#include <fcntl.h>
#include <signal.h>
#include <string.h>

typedef struct {
    int id, times_eaten;
    pid_t pid;
    int *dead_flag;
} t_philo;

typedef struct {
    t_philo *philo;
    sem_t *forks, *print_semaphore, *dead_semaphore, *eat_semaphore;
    int num_of_philo, time_to_die, time_to_eat, time_to_sleep, num_of_meals, dead_flag;
    long start_time, last_meal;
    pthread_t monitor_thread;
} t_data;

long get_time(void) {
    struct timeval tv;
    gettimeofday(&tv, NULL);
    return tv.tv_sec * 1000 + tv.tv_usec / 1000;
}

void init_values(t_data *data, char *argv[]) {
    data->philo->id = 0;
    data->start_time = get_time();
    data->last_meal = get_time();
    data->num_of_philo = atoi(argv[1]);
    data->time_to_die = atoi(argv[2]);
    data->time_to_eat = atoi(argv[3]);
    data->time_to_sleep = atoi(argv[4]);
    data->num_of_meals = argv[5] ? atoi(argv[5]) : -1;
    data->philo->dead_flag = &data->dead_flag;
}

void init_semaphores(t_data *data) {
    sem_unlink("/forks");
    sem_unlink("/print_sem");
    sem_unlink("/dead_sem");
    data->forks = sem_open("/forks", O_CREAT, 0644, data->num_of_philo);
    data->print_semaphore = sem_open("/print_sem", O_CREAT, 0644, 1);
    data->dead_semaphore = sem_open("/dead_sem", O_CREAT, 0644, 1);
}

void check_dead(t_data *data) {
    sem_wait(data->eat_semaphore);
    if (get_time() - data->last_meal >= data->time_to_die) {
        sem_wait(data->print_semaphore);
        printf("%ld philo[%d] has died\n", get_time() - data->start_time, data->philo->id);
        data->dead_flag = 1;
        exit(1);
    }
    sem_post(data->eat_semaphore);
}

void *monitor(void *arg) {
    t_data *data = (t_data *)arg;
    while (1) {
        check_dead(data);
        if (data->dead_flag) exit(0);
        usleep(100);
    }
    return NULL;
}

void timed_action(long time, t_data *data, char *msg) {
    long start = get_time();
    printf("%ld philo[%d] %s\n", get_time() - data->start_time, data->philo->id, msg);
    while (get_time() - start < time) {
        sem_wait(data->dead_semaphore);
        if (data->dead_flag) {
            sem_post(data->dead_semaphore);
            break;
        }
        sem_post(data->dead_semaphore);
        usleep(10);
    }
}

void eating(t_data *data) {
    sem_wait(data->forks);
    sem_wait(data->forks);
    data->last_meal = get_time();
    timed_action(data->time_to_eat, data, "is eating");
    data->philo->times_eaten++;
    sem_post(data->forks);
    sem_post(data->forks);
}

void philosopher_life(t_data *data) {
    data->last_meal = get_time();
    if (pthread_create(&data->monitor_thread, NULL, monitor, data)) {
        fprintf(stderr, "Error creating monitor thread\n");
        exit(1);
    }
    if (data->philo->id % 2 == 0) usleep(5);
    while (1) {
        eating(data);
        if (data->dead_flag || (data->num_of_meals != -1 && data->philo->times_eaten >= data->num_of_meals)) exit(0);
        timed_action(data->time_to_sleep, data, "is sleeping");
        printf("%ld philo[%d] is thinking\n", get_time() - data->start_time, data->philo->id);
    }
    pthread_join(data->monitor_thread, NULL);
}

void create_processes(t_data *data) {
    int i = 0;
    while (i < data->num_of_philo) {
        data->philo->pid = fork();
        if (data->philo->pid == 0) {
            data->philo->id = i + 1;
            philosopher_life(data);
        } else if (data->philo->pid == -1) {
            fprintf(stderr, "Fork error\n");
            exit(1);
        }
        i++;
    }
}

void wait_and_kill(t_data *data) {
    int status, i = 0;
    while (i < data->num_of_philo) {
        waitpid(-1, &status, 0);
        if (status) {
            for (int j = 0; j < data->num_of_philo; j++)
                kill(data->philo[j].pid, SIGINT);
            break;
        }
        i++;
    }
    sem_close(data->forks);
    sem_close(data->print_semaphore);
    sem_close(data->dead_semaphore);
    sem_unlink("/forks");
    sem_unlink("/print_sem");
    sem_unlink("/dead_sem");
    free(data->philo);
}

int main(int argc, char *argv[]) {
    if (argc < 5 || argc > 6) {
        fprintf(stderr, "Usage: ./philo_bonus [number_of_philosophers] [time_to_die] [time_to_eat] [time_to_sleep] [num_of_meals]\n");
        return 1;
    }
    t_data data;
    data.philo = malloc(sizeof(t_philo) * atoi(argv[1]));
    if (!data.philo) {
        perror("Malloc error");
        return 1;
    }
    init_values(&data, argv);
    init_semaphores(&data);
    create_processes(&data);
    wait_and_kill(&data);
    return 0;
}
