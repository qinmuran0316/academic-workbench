# CAD and engineering drawing mode

## Intake

Extract units, coordinate system, origin, layers, line types, scale, title block, dimensions, tolerances, projection, required views, file format, and native CAD version. If the task gives a sketch or image, distinguish observed geometry from inferred geometry.

## Geometry contract

Create editable geometry with named layers and explicit dimensions. Check coordinates, radii/diameters, closed profiles, constraints, text/arrow readability, and unit metadata. For a 120×80 mm plate with a Ø30 center hole at (60,40) and four Ø10 holes at (15,15), (105,15), (105,65), (15,65), independently verify the five circles and outer bounds; the net area is `120×80 − π×15² − 4×π×5²` mm².

## File and validation rules

Prefer the requested native editable format. DXF can be parsed and geometry-audited with `scripts/inspect_dxf.py`; SVG/PDF previews are supplementary. Do not call a DXF parse “AutoCAD validation”. State whether AutoCAD/BricsCAD/FreeCAD or another native viewer opened and checked the file. A text file renamed `.dwg` is not a DWG.

## Engineering honesty

Do not infer manufacturing tolerances, material, load capacity, or code compliance from a simple drawing. Put assumptions in the drawing notes/report and flag any missing standard, projection, or template.
