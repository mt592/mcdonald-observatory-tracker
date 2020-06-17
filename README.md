# McDonald Observatory Status Tracker

<img src="mcdonald_obs_moon.jpeg" alt="Moon from McDonald Observatory 36 inch telescope" width="250" height="250"/>

This simple tracker sends users an email detailing whether or not the [McDonald Observatory](https://mcdonaldobservatory.org/) has potentially re-opened to visitors, and notifies users of any new press releases. 

The code accesses the McDonald Observatory's visitors page to see if the "closed to visitors" notice has been removed.


## Getting Started

### Installation
```bash
git clone https://github.com/mt592/mcdonald-observatory-tracker.git
```
### Usage
1. `cd mcdonald_obs_tracker`
2. Find the **config_example.ini** file in the **/ref** folder, and rename it to **config.ini**. Fill in the senders email address and secret key (see below). Fill in the recipients email address.  
3. `python email_driver.py`


### Using gmail app passwords

If you have a gmail account, you can create an app password by logging into your gmail account [here](https://myaccount.google.com/u/1/apppasswords?pli=1&rapt=AEjHL4PXlfTR51trGXZd8xd_r9gpZwZ_2RH7KhwRQI27yzAhofxqdY9pVpUqqGUvrZZJOamyy1CgB_4C1YvASGudq3q4DU6CBQ). Using an app password will allow you to send emails without logging in with 2-Step verificatin.

### Versions

In a future release this tracker will be extended to notify users of when telescope viewing dates are released to the public. Viewing slots are limited, so immediate notice is always helpful in securing a spot to view out of the research grade telescopes. 

### Authors and Acknowledgment

Author: **Michelle Turovsky**
Acknowledgment: David Okwii on [stackoverflow](https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python)

