# 2024 Fall Miniproject assignment by Mete Gumusayak and Jared Solis

### Exercise 1

Got the min_bright by running the Pico with bright light and the max_bright by running the Pico while covering the sensor.
max_bright = 19400, min_bright = 40000

Video: https://drive.google.com/file/d/1Ri7sSFddFn-eF9AiZLlQ7nOPBY0zaMvt/view?usp=sharing

### Exercise 2
We chose the song "Through the Fire and the Flames" by Dragon Force and then used a frequency to note converter. Then we stored the notes in a list and played them:

Video: https://drive.google.com/file/d/1Eu1Cojsxc00HLmXDOVwNFNJTZdeae4qh/view?usp=sharing
 
 ```python
freqs = [261, 293, 311, 261, 293, 311, 349, 311, 392, 311, 349, 293, 311, 261, 293, 233]
```


### Exercise 3
We changed N from 3 to 10

We used the min and max functions, calculated the average times, and then saved the data to a dict. 
This data was then sent to Firebase realtime database with a post request
We added functionality to connect to the wifi

Video: https://drive.google.com/file/d/1fXfTO-Ao6U2YbK1Soz-hcoY6CnwMKEnp/view?usp=sharing
