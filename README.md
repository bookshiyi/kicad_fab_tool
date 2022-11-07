
| **KiCad fabrication tool** |
|:-----:|

</div>

## Features
1.	Generates gerber files in correct format for production
2.	Generates BOM file in correct format for production
3.	Generates Pick and Place file in correct format for assembly
4.	Generates IPC netlist file

## Installation

### Official Installation
Open the "Plugin and Content Manager" from the KiCad main menu and install the "<ins>Fabrication Tool</ins>" plugin from the selection list.

### Manual installation
Download the latest ZIP file from https://github.com/bookshiyi/kicad_fab_tool. Open the "Plugin and Content Manager" from the KiCads main window and install the ZIP file via "Install from File".

## Usage
Click on the Fabrication Tool ![logo](./plugins/icon.png) button on the top tool box inside KiCad pcb editor (pcbnew).

## Options

### Include Component Part Number in Production Files
Add an 'LCSC Part #'* field with the LCSC component part number to the symbol's fields property.

![mpn](./assets/mpn.png) 

#### Primary Fields*:
| 'LCSC Part #' | 'JLCPCB Part #' |
| --- | --- |

_The fields will be query in the order denoted above._

#### Fallback Fields*:
| 'LCSC' | 'JLC' | 'MPN' | 'Mpn' | 'mpn' |
| --- | --- | --- | --- | --- |

_The fields will be query in the order denoted above._

### Ignore Footprint in Production Files
Select 'Exclude from board' or 'Exclude from BOM' in the symbol's attributes property in order to ignore the footprint from the relevant file.

![attributes](./assets/attributes.png) 

Select 'Exclude from position files' or 'Exclude from BOM' in the footprint's fabrication attributes property in order to ignore the footprint from the relevant file.

![fabrication](./assets/fabrication.png) 

### Rotate a Component
The rotation of components in KiCad Footprints does not always match the orientation in the JLC library.
Add an 'JLC Rotation Offset' field with an counter-clockwise orientation offset in degrees to correct this.

![rotation-jlc](./assets/rotation-jlc.png) 

If the JLC preview shows a footprint like this, enter a rotation offset of -90 to rotate pin 1 to the lower right corner.

![rotation](./assets/rotation.png) 

#### Primary Fields*:
| 'JLCPCB Rotation Offset' |
| --- |

_The fields will be queried in the order denoted above._

#### Fallback Fields*:
| 'JlcRotOffset' | 'JLCRotOffset' |
| --- | --- |

_The fields will be queried in the order denoted above._

## Thanks

[Benny Megidish](https://github.com/bennymeg/)
