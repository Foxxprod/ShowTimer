#define MyAppName "ShowTimer"
#define MyAppVersion "1.1"
#define MyAppPublisher "Foxx Production"
#define MyAppURL "https://www.foxxprod.fr/"
#define MyAppExeName "ShowTimer_1.1.exe"

[Setup]
AppId={{7B5008C8-D46B-40FE-934B-BE4CE4DB3605}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
UninstallDisplayIcon={app}\{#MyAppExeName}
ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible
DisableProgramGroupPage=no
LicenseFile=C:\Users\Perso-PC\Documents\GitHub\TIMER_PCP\LICENSE.txt
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=C:\Users\Perso-PC\Documents\GitHub\TIMER_PCP\installer
OutputBaseFilename=ShowTimer_1.1_setup
SetupIconFile=C:\Users\Perso-PC\Documents\GitHub\TIMER_PCP\icon\icon.ico
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: checkedonce
Name: "startmenuicon"; Description: "Créer un raccourci dans le menu Démarrer"; GroupDescription: "{cm:AdditionalIcons}"; Flags: checkedonce

[Files]
Source: "C:\Users\Perso-PC\Documents\GitHub\TIMER_PCP\output\ShowTimer\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\Perso-PC\Documents\GitHub\TIMER_PCP\output\ShowTimer\_internal\*"; DestDir: "{app}\_internal"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
; Raccourcis menu Démarrer (optionnels)
Name: "{autoprograms}\{#MyAppName}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: startmenuicon
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
; Raccourci désinstalleur — toujours créé dans le menu Démarrer
Name: "{autoprograms}\{#MyAppName}\Désinstaller {#MyAppName}"; Filename: "{uninstallexe}"

[Registry]
; Association de l'extension .stshow
Root: HKA; Subkey: "Software\Classes\.stshow";                                          ValueType: string; ValueName: ""; ValueData: "FoxxProduction.ShowFile";               Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\FoxxProduction.ShowFile";                          ValueType: string; ValueName: ""; ValueData: "ShowTimer Show File";                   Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\FoxxProduction.ShowFile\DefaultIcon";              ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppExeName},0"
Root: HKA; Subkey: "Software\Classes\FoxxProduction.ShowFile\shell\open\command";       ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppExeName}"" ""%1"""

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
