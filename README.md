acq400_regression

a suite of tests to test D-tacq uut functionality and save the results



test_handler
    -used to invoke each test, collect data and store results
uut_handler
    -used to control uuts asyncrosonousl way 
misc
    -stand alone helper functions 







test results are saved in named dirs 

//Local saved results format
results/
├── ACQ435ELF/
│   ├── 240416144229/
│   |   ├── results.json
│   |   ├── fpga.txt
│   |   ├── firmware.txt
│   |   ├── post_trg111
│   |   |   ├── uut1.timestamp.2CH.dat
│   |   |   ├── uut1.timestamp.png
│   |   |   ├── uut2.timestamp.2CH.dat
│   |   |   ├── uut2.timestamp.png
│   |   ├── prepost_trg111_evt111
│   |   |   ├── uut1.timestamp.2CH.dat
│   |   |   ├── uut1.timestamp.png
│   |   |   ├── uut2.timestamp.2CH.dat
│   |   |   ├── uut2.timestamp.png
│   |   ├── rtm_trg111_evt111
│   |   |   ├── uut1.timestamp.2CH.dat
│   |   |   ├── uut1.timestamp.png
│   |   |   ├── uut2.timestamp.2CH.dat
│   |   |   ├── uut2.timestamp.png

//JSON Example format
{
    "uuts": [ # list of uuts and their configuration
        {
            "uut_name": "acq2106_007",
            "fpga": "ACQ2106_TOP_08_ff_ff_ff_ff_ff_9511_64B",
            "fpga_timestamp": "2021/09/14",
            "version": 694,
            "firmware": "acq400-694-20240419111926",
            "serial": "CE4160007",
            "model": "acq2106",
            "clk": 19999594,
            "nchan": 8,
            "data_size": 2,
            "master": true,
            "wr": false,
            "modules": [
                {
                    "location": 1,
                    "model": "ACQ480ELF N=8 M=08",
                    "serial": "E48010086",
                    "nchan": 8,
                    "full_model": "ACQ480ELF N=8 M=08"
                }
            ]
        }
    ],
    "feature_tests": [
        {
            "type": "post",
            "channels": [
                1
            ],
            "tolerance": 0.035,
            "cycles": 1,
            "post": 100000,
            "freq": 999,
            "voltage": 2.5,
            "trigger": "1,0,0",
            "timestamp": "240419145744",
            "run": "1/1",
            "result": "pass",
            "subtests": [
                {
                    "hostname":"acq2106_007",
                    "wave_synchronous": {
                        "passed": True,
                    },
                    "spad_nogap": {
                        "passed": True,
                    },
                },
                {
                    "hostname":"acq2106_123",
                    "wave_synchronous": {
                        "passed": True,
                    },
                    "spad_nogap": {
                        "passed": True,
                    },
                }
                
            }
        },
    ],
}