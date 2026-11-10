# Package the skill folder into dist\denvora-ai-skills.skill (a zip archive)
# and dist\denvora-ai-skills.zip, for uploading to Claude (Settings > Skills)
# or attaching to a GitHub Release.
#
# Usage (PowerShell): .\scripts\package-skill.ps1
$ErrorActionPreference = 'Stop'

$Root      = Split-Path -Parent $PSScriptRoot
$SkillName = 'denvora-ai-skills'
$SkillDir  = Join-Path $Root "skills\$SkillName"
$Dist      = Join-Path $Root 'dist'

if (-not (Test-Path (Join-Path $SkillDir 'SKILL.md'))) {
    throw "SKILL.md not found in $SkillDir"
}

New-Item -ItemType Directory -Force -Path $Dist | Out-Null
$Zip   = Join-Path $Dist "$SkillName.zip"
$Skill = Join-Path $Dist "$SkillName.skill"
Remove-Item -Force -ErrorAction SilentlyContinue $Zip, $Skill

# Build the zip manually instead of using Compress-Archive: Windows PowerShell 5.1
# writes entry names with backslashes, which break on macOS/Linux extractors.
# Entries are stored as "denvora-ai-skills/<relative path>" with forward slashes.
Add-Type -AssemblyName System.IO.Compression
Add-Type -AssemblyName System.IO.Compression.FileSystem

$Archive = [System.IO.Compression.ZipFile]::Open($Zip, [System.IO.Compression.ZipArchiveMode]::Create)
try {
    Get-ChildItem -Path $SkillDir -Recurse -File |
        Where-Object { $_.Name -notin @('.DS_Store', 'Thumbs.db', 'desktop.ini') } |
        ForEach-Object {
            $Relative  = $_.FullName.Substring($SkillDir.Length).TrimStart('\', '/') -replace '\\', '/'
            $EntryName = "$SkillName/$Relative"
            [System.IO.Compression.ZipFileExtensions]::CreateEntryFromFile(
                $Archive, $_.FullName, $EntryName,
                [System.IO.Compression.CompressionLevel]::Optimal) | Out-Null
        }
}
finally {
    $Archive.Dispose()
}

Copy-Item $Zip $Skill

Write-Host "Created:"
Write-Host "  $Skill"
Write-Host "  $Zip"
