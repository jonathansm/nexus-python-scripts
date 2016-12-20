# nexus-python-scripts

Collection of Python scripts for nexus switches that I find useful.

You can run python scripts right from the cmd line 
```switch# python bootflash:scriptname.py```

or you can use the scheduler and have the python script run whenever you want

1. Enable the feature ```switch(config)# feature scheduler```
2. Create a new job ```switch(config)# scheduler job name jobname```
3. Set what the scheduler will do ```switch(config-job)# python bootflash:scriptname.py```
4. Set when to run the scheduler ```time daily 23:00```
  1. See this great PDF for other scheduler options https://www.cisco.com/c/en/us/td/docs/switches/datacenter/sw/5_x/nx-os/system_management/configuration/guide/sm_nx_os_cg/sm_8scheduler.pdf
