from crontab import CronTab

def main():
    cron = CronTab(user='root')
    job = cron.new(command="cd '~/mcdonald_observatory_tracker' && ~/anaconda3/bin/python email_driver.py")
    job.dow.on('SUN')
    cron.write()

if __name__ == '__main__':
    main()