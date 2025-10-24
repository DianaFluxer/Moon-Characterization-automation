# # -*- coding: utf-8 -*-
# """
# Created on Fri Oct 24 14:27:06 2025

# @author: diana.dimitrova
# """
# from pyvisa import VisaIOError
# from qcodes import Station
# from qcodes.instrument.base import Instrument
# Instrument.close_all()

# from qcodes.dataset import (
#     Measurement,
#     initialise_database,
#     new_experiment,
#     plot_dataset,
# )
# from qcodes.instrument_drivers.Keithley import Keithley2450

# keithley = Keithley2450("keithley", "TCPIP0::10.1.2.80::inst0::INSTR")

# keithley.reset()

# keithley.source.function("voltage")
# keithley.source.auto_range(True)
# keithley.source.limit(10)

# keithley.source.sweep_setup(-3, 0.01, 10)

# keithley.sense.function("current")

# station = Station()

# station.add_component(keithley)
# setup = station.snapshot()

# initialise_database()
# experiment = new_experiment(name="Keithley_2450_example", sample_name="SA970D")

# meas = Measurement(exp=experiment, station=station, name="voltage_sweep")
# meas.register_parameter(keithley.sense.sweep)

# with meas.run() as datasaver:
#     datasaver.add_result(
#         (keithley.source.sweep_axis, keithley.source.sweep_axis()),
#         (keithley.sense.sweep, keithley.sense.sweep()),
#     )
    

#     dataid = datasaver.run_id

# plot_dataset(datasaver.dataset)

# ds = datasaver.dataset

# # Convert to a pandas DataFrame
# df = ds.to_pandas_dataframe()

# # Save to CSV (in the current working folder)
# df.to_csv("keithley_IV_data.csv", index=False)


# # Preview a few rows (safe for Spyder)
# print(df.head())


from pyvisa import VisaIOError
from qcodes import Station
from qcodes.instrument.base import Instrument

Instrument.close_all()

from qcodes.dataset import (
    Measurement,
    initialise_database,
    new_experiment,
    plot_dataset,
)
from qcodes.instrument_drivers.Keithley import Keithley2450

keithley = Keithley2450("keithley", "TCPIP0::10.1.2.80::inst0::INSTR")

keithley.reset()

keithley.source.function("voltage")
keithley.source.auto_range(True)
keithley.source.limit(10)
keithley.source.sweep_setup(-3, 0.01, 10)
keithley.sense.function("current")

station = Station()
station.add_component(keithley)
setup = station.snapshot()

initialise_database()
experiment = new_experiment(name="Keithley_2450_example", sample_name="SA970D")

meas = Measurement(exp=experiment, station=station, name="voltage_sweep")
meas.register_parameter(keithley.sense.sweep)

with meas.run() as datasaver:
    datasaver.add_result(
        (keithley.source.sweep_axis, keithley.source.sweep_axis()),
        (keithley.sense.sweep, keithley.sense.sweep()),
    )
    

    dataid = datasaver.run_id

plot_dataset(datasaver.dataset)

ds = datasaver.dataset

# Convert to a pandas DataFrame
df = ds.to_pandas_dataframe()

# Save to CSV (in the current working folder)
df.to_csv("keithley_IV_data.csv", index=False)


# Preview a few rows (safe for Spyder)
print(df.head())