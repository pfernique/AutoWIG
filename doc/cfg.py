c.NbConvertApp.notebooks = ["examples/basic.ipynb",
                            "examples/subset.ipynb"]

c.ExecutePreprocessor.timeout = 60

# conda install python-autowig python-clanglite -c statiskit -c conda-forge && git clone https://github.com/StatisKit/AutoWIG.git && cd AutoWIG/doc && jupyter nbconvert --config cfg.py --to notebook --execute --inplace
