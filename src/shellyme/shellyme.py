import click
import ShellyPy


@click.command()
@click.option('--device-ip')
def cli(device_ip):
    """Scan Device for status """
    print(f"Connecting to {device_ip}")
    device=ShellyPy.Shelly(device_ip)
    print(device.status())
    deviceMeter = device.meter(0)
    power=deviceMeter['power']
    print(f'{device_ip} power={power}') 

if __name__ == '__main__':
    cli()