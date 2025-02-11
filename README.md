
---

# M3U4U Customization Transfer Script

## Overview

This script helps **restore lost customizations** after syncing your M3U4U playlist. When an IPTV provider updates all channel URLs, M3U4U removes any custom sorting, logos, hidden channels, and group settings. This script transfers all those settings from an **old backup** to a **new backup**, keeping the new URLs while restoring your previous customizations.

## How It Works

### 1. **Prerequisites:**
- You must have **an old backup** (before syncing) that contains your preferred customizations.
- You must create **a new backup** (after syncing) to capture the latest URLs, name changes, and structure updates.

### 2. **What This Script Does:**
- It **uses the new backup as the base**, keeping its URLs, names, and structure.
- It **transfers all customization settings** from the old backup to the corresponding channels in the new backup.
- It **outputs a new JSON file** (`output.json`) that you can restore in M3U4U.

### 3. **What Gets Transferred:**
- Channel order
- Custom logos
- Custom names (if previously set)
- Hidden channels
- Group assignments
- Any other customization settings inside the `"Customization"` field

## Usage

1. **Run the script with:**
   ```bash
   python transfer_customization.py old.json new.json output.json
   ```
   - `old.json`: Your backup before the sync (containing desired customizations).
   - `new.json`: Your latest backup after the sync (containing the updated URLs).
   - `output.json`: The final merged JSON file.

2. **Replacing the JSON in the Backup ZIP:**
   - After running the script, locate the zipped backup file from M3U4U.
   - Open the `.zip` file and delete the existing `.json` file inside.
   - Rename `output.json` to match the name of the deleted file exactly.
   - Place the renamed file inside the `.zip` and save it.

3. **Restoring the Backup:**
   - Upload (restore) the modified `.zip` file back to M3U4U to restore your customizations.

## Notes

- **Ensure exact name matching** between channels for proper customization transfer.
- **Do not modify the new URLs**—the script keeps them unchanged.
- **Non-ASCII characters (e.g., ñ, é) are preserved** in the output.
- **Always back up your data** before running the script.