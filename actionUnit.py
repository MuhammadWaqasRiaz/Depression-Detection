
import pandas as pd
import os

# Define the expected column name mapping
column_mapping = {
    "Inner Brow Raise (AU1)": "InnerBrowRaiseAU1",
    "Outer Brow Raise (AU2)": "OuterBrowRaiseAU2",
    "Brow Lowerer (AU4)": "BrowLowererAU4",
    "Upper Lid Raiser (AU5)": "UpperLidRaiserAU5",
    "Cheek Raiser (AU6)": "CheekRaiserAU6",
    "Nose Wrinkler (AU9)": "NoseWrinklerAU9",
    "Upper Lip Raiser (AU10)": "UpperLipRaiserAU10",
    "Lip Corner Puller (AU12)": "LipCornerPullerAU12",
    "Dimpler (AU14)": "DimplerAU14",
    "Lip Corner Depressor (AU15)": "LipCornerDepressorAU15",
    "Chin Raiser (AU17)": "ChinRaiserAU17",
    "Lip Stretcher (AU20)": "LipStretcherAU20",
    "Lip Tightener (AU23)": "LipTightenerAU23",
    "Lip Pressor (AU24)": "LipPressorAU24",
    "Lips Part (AU25)": "LipsPartAU25",
    "Jaw Drop (AU26)": "JawDropAU26",
    "Mouth Stretch (AU27)": "MouthStretchAU27",
    "Lip Suck (AU28)": "LipSuckAU28",
    "Blink (AU45)": "BlinkAU45",
    "Head Turn Left": "HeadTurnLeft"
}

# Input/output folder paths
input_folder = "6may_Action_Units"
output_folder = "6may_New_Action_Units_after_trim"
os.makedirs(output_folder, exist_ok=True)

# Process each file
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        filepath = os.path.join(input_folder, filename)

        df = pd.read_csv(filepath)

        # Clean column names (strip spaces and normalize)
        df.columns = df.columns.str.strip()

        # Select only columns present in the mapping
        common_cols = [col for col in df.columns if col in column_mapping]
        df = df[common_cols]

        # Rename columns using mapping
        df.rename(columns=column_mapping, inplace=True)

        # Add missing columns with NaN values (if any expected column is missing)
        for old_name, new_name in column_mapping.items():
            if new_name not in df.columns:
                df[new_name] = pd.NA

        # Reorder columns to match the expected output order
        df = df[list(column_mapping.values())]

        # Add 'Stage' column
        df["Stage"] = "Normal"

        # Save result
        output_path = os.path.join(output_folder, f"processed_{filename}")
        df.to_csv(output_path, index=False)

print("✅ All files processed with robust column matching.")
