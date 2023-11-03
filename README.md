### nRF for VSCode installation instructions

* https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/installation/assistant.html

### A really nice intro to nRF Connect SDK and Zephyr RTOS

* https://academy.nordicsemi.com/courses/nrf-connect-sdk-fundamentals/

### Some nice examples for the dwm1001

* https://github.com/RT-LOC/zephyr-dwm1001

* Note: The include paths of the examples don't match the 'anchor' and 'tag' projects, so you'll have to modify the examples to match the 'anchor' and 'tag' includes. Also, replace 'Sleep' calls with 'k_msleep' and change 'dw_main' to 'main'. Look at the 'anchor' and 'tag' projects for specifics on how to make these changes.