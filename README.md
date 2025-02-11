
---

# 🚀 M3U4U Customization Transfer Script

## 🎯 Overview

When your IPTV provider updates channel URLs, your **logos, hidden channels, group settings, and sorting** are wiped out. 

✨ **This script fixes that!** ✨  
It restores all your **personalized settings** by transferring them from an **old backup** to a **new backup**, keeping your updated URLs intact while bringing back your custom preferences.

---

## 🔧 How It Works

### ✅ **Step 1: Get Your Backups Ready**
Before running the script, you’ll need:
✔ **An old backup** (before syncing) – this contains your customizations.  
✔ **A new backup** (after syncing) – this contains the latest URLs and channel structure.  

### 🔄 **Step 2: What This Script Does**
🔹 Uses the **new backup** as the foundation, keeping its updated URLs and structure.  
🔹 Transfers **all your customizations** from the old backup to the corresponding channels in the new backup.  
🔹 Outputs a final **merged JSON file** (`output.json`) that **restores your settings** when uploaded back into M3U4U.  

### 🎛 **Step 3: What Gets Restored**
✅ Channel order  
✅ Custom logos  
✅ Custom names (if previously set)  
✅ Hidden channels  
✅ Group assignments  
✅ Any other settings in the `"Customization"` field  

---

## 🚀 Usage Guide

### 💻 **Run the Script**
Run the following command in your terminal or command prompt:

```bash
python transfer_customization.py old.json new.json output.json
```
- `old.json` → Your **pre-sync backup** (with your customizations).  
- `new.json` → Your **post-sync backup** (with updated URLs & structure).  
- `output.json` → Your **final JSON file**, ready to restore in M3U4U.  

---

## 📂 **Replacing the JSON in the Backup ZIP**  
After running the script, follow these steps to **apply the restored settings**:

1. **Locate** your most recent **M3U4U backup ZIP file**.  
2. **Open** the `.zip` file and **delete** the existing `.json` file inside.  
3. **Rename** `output.json` **to match the name of the deleted file exactly**:  
   - Ensure that the `DateCreated` and `PlaylistCode` (both located at the top) match the original file.  
4. **Place** the renamed file back into the `.zip` and save it.  

---

## 📤 **Restoring Your Backup**
Finally, upload the modified `.zip` file back into **M3U4U** to fully restore your **logos, hidden channels, and group settings** 🎉.  

---

## 📝 Important Notes

⚠ **Make sure channel names match exactly** for proper customization transfer.  
⚠ **Do not modify the new URLs**—the script ensures they stay up to date.  
⚠ **Special characters (e.g., ñ, é) are preserved** to avoid encoding issues.  
⚠ **Always keep a backup** of your data before running the script.  

---