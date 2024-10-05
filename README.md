# Daily
Jest to kolejna aplikacja służąca do planowania. Łączy ze sobą elementy kalendarza, plannera oraz wybranych elementów bullet journala m.in. śledzenie nastroju, snu oraz pogody.
>Projekt jest na etapie prototypowania.
***

## Funkcje występujące w programie **prototype.py**:

 - **add_task_to_file** - odbiera listę z danymi zadania i zapisuje je do pliku **tasks.txt**

 - **new_task** - umożliwia tworzenie nowego zadania przez użytkownika. Zadanie jest przesyłane następnie do funkcji **add_task_to_file**

 - **read_tasks** - odczytuje zadania i segreguje je według daty - zadania z aktualną datą są w zadaniach na dany dzień, natomiast te, których data minęła a nie zostały wykonane, znajdują się w zaległych. Przyszłe zadania nie są wyświetlane.

 - **update_status** - pozwala na zaktualizowanie statusu zadania po jego id (uzyskiwane przy odczycie zadań przez **read_tasks**) oraz dodatkowo zlicza zadania zrobione danego dnia.

 - **delete_tasks** - usuwa wykonane zadania z poprzednich dni z pliku **tasks** oraz zeruje liczbę zrobionych zadań kolejnego dnia.

 - **display_n_done** - wyświetla liczbę zrobionych danego dnia tasków

 - **check_files** - sprawdza, czy niezbędne pliki istnieją, jeśli nie, to je tworzy
