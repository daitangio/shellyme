import click
import ShellyPy


@click.command()
@click.option('--device-ip')
@click.option('--turn-on/--turn-off', default=None)
def cli(device_ip, turn_on):
    """Scan Plug S Device for status, optionally turn it on/off """
    print(f"Connecting to {device_ip}")
    device=ShellyPy.Shelly(device_ip)
    print("Status",device.status())
    print("Hook Events Supported", device.hookList())
    print("Script status", device.scriptList())

    if(turn_on==True):
        print("Turning on...")
        print(device.relay(0, turn=True))
    elif turn_on==False:
        print("Turning off...")
        print(device.relay(0, turn=False))  
    else:
        print("Switch status:", device.relay(0))      
    #deviceMeter = device.meter(0)
    #power=deviceMeter['power']
    #print(f'{device_ip} power={power}') 

if __name__ == '__main__':
    cli()