@echo off
REM ┌── Author's Information ────────────────────────────────────────────────────────┐
REM │                                                                                │
REM │   Marin Grubišić                                                               │
REM │   Assistant Professor | MEng, PhD, PE                                          │
REM │   University of Osijek, Faculty of Civil Engineering and Architecture Osijek   │
REM │   Department of Technical Mechanics                                            │
REM │   3 Vladimir Prelog Street (University Campus), Office II.26 (2nd floor)       │
REM │   HR-31000 Osijek, Croatia, Europe                                             │
REM │                                                                                │
REM │   E-mail:   marin.grubisic@gfos.hr    │ marin.grubisic@gmail.com               │
REM │   Tel.:     +385 95 823 15 75         │ +385 91 224 07 92                      │
REM │   Web:      www.maringrubisic.com     │ github.com/mgrubisic                   │
REM │   Social:   linkedin.com/in/mgrubisic │ x.com/mgrubisic                        │
REM │   Update:   5.6.2014. / 29.4.2017.                                             │
REM │                                                                                │
REM └────────────────────────────────────────────────────────────────────────────────┘

cd C:\GITHUB_Master\HystereticCurveAnalysis

echo Dodavanje izmjena u staging area...
git add .

echo Commitanje izmjena...
git commit -m "Update C:\GITHUB_Master\HystereticCurveAnalysis"

echo Slanje izmjena na GitHub...
git push origin main

echo Povlacenje najnovijih izmjena iz GitHub repozitorija...
git pull origin main

echo Gotovo!
pause
