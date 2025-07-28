import click
import ShellyPy


@click.command()
@click.option('--device-ip')
def cli(device_ip):
    """Scan Device for status """
    device=ShellyPy.Shelly(device_ip)
    deviceMeter = device.meter(0)
    power=deviceMeter['power']
    print(f'{device_ip} power={power}') 

