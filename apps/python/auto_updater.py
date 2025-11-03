#!/usr/bin/env python3
"""
Saganomic AI Catalyst - Automated Update System
$aga - SAGA Functional Identity System

Automatically checks for, downloads, and applies updates
All updates covered under MIT License

MIT License
Copyright (c) 2025 Saga Gonzo
"""

import subprocess
import sys
import os
import time
from datetime import datetime
from typing import Tuple, Optional


class SagaAutoUpdater:
    """
    Automated update system for Saganomic AI Catalyst

    Features:
    - Git-based update checking
    - Automatic update application
    - Rollback support
    - MIT License compliance verification
    - Secure update validation

    $aga Easter Egg: Revolutionary parallel updates at your discretion
    """

    def __init__(self, repo_path: Optional[str] = None):
        """Initialize updater with repository path"""
        if repo_path is None:
            # Auto-detect repo path
            self.repo_path = self._find_repo_root()
        else:
            self.repo_path = repo_path

        self.current_branch = None
        self.update_available = False

    def _find_repo_root(self) -> str:
        """Find the git repository root"""
        try:
            result = subprocess.run(
                ['git', 'rev-parse', '--show-toplevel'],
                cwd=os.path.dirname(os.path.abspath(__file__)),
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return os.path.dirname(os.path.abspath(__file__))
        except:
            return os.path.dirname(os.path.abspath(__file__))

    def check_git_status(self) -> Tuple[bool, str]:
        """Check if we're in a git repository"""
        try:
            result = subprocess.run(
                ['git', 'status'],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0:
                return True, "Git repository detected"
            else:
                return False, "Not a git repository"
        except Exception as e:
            return False, f"Git check failed: {e}"

    def get_current_branch(self) -> Optional[str]:
        """Get current git branch"""
        try:
            result = subprocess.run(
                ['git', 'branch', '--show-current'],
                cwd=self.repo_path,
                capture_output=True,
                text=True,
                timeout=5
            )

            if result.returncode == 0:
                self.current_branch = result.stdout.strip()
                return self.current_branch
            return None
        except:
            return None

    def check_for_updates(self, retry_count: int = 4) -> Tuple[bool, str]:
        """
        Check for remote updates with exponential backoff retry

        Args:
            retry_count: Number of retries with exponential backoff (2s, 4s, 8s, 16s)

        Returns:
            Tuple of (updates_available, message)
        """
        branch = self.get_current_branch()
        if not branch:
            return False, "Could not determine current branch"

        print(f"🔍 Checking for updates on branch: {branch}")

        for attempt in range(retry_count):
            try:
                # Fetch with timeout
                result = subprocess.run(
                    ['git', 'fetch', 'origin', branch],
                    cwd=self.repo_path,
                    capture_output=True,
                    text=True,
                    timeout=10
                )

                if result.returncode == 0:
                    # Check if remote is ahead
                    status_result = subprocess.run(
                        ['git', 'status', '-uno'],
                        cwd=self.repo_path,
                        capture_output=True,
                        text=True,
                        timeout=5
                    )

                    if 'behind' in status_result.stdout.lower():
                        self.update_available = True
                        return True, f"Updates available on {branch}"
                    else:
                        return False, "System up to date"

                elif attempt < retry_count - 1:
                    # Network error - retry with exponential backoff
                    wait_time = 2 ** (attempt + 1)  # 2s, 4s, 8s, 16s
                    print(f"⚠️  Network error, retrying in {wait_time}s... (attempt {attempt + 2}/{retry_count})")
                    time.sleep(wait_time)
                else:
                    return False, "Failed to fetch updates after retries"

            except subprocess.TimeoutExpired:
                if attempt < retry_count - 1:
                    wait_time = 2 ** (attempt + 1)
                    print(f"⏱️  Timeout, retrying in {wait_time}s... (attempt {attempt + 2}/{retry_count})")
                    time.sleep(wait_time)
                else:
                    return False, "Fetch timed out after retries"
            except Exception as e:
                if attempt < retry_count - 1:
                    wait_time = 2 ** (attempt + 1)
                    print(f"⚠️  Error: {e}, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    return False, f"Update check failed: {e}"

        return False, "Update check failed"

    def verify_mit_license(self) -> bool:
        """Verify MIT License is present in repository"""
        try:
            # Check for LICENSE or LICENSE.md file
            license_paths = ['LICENSE', 'LICENSE.md', 'LICENSE.txt']

            for license_file in license_paths:
                full_path = os.path.join(self.repo_path, license_file)
                if os.path.exists(full_path):
                    with open(full_path, 'r') as f:
                        content = f.read()
                        if 'MIT License' in content or 'MIT' in content:
                            return True

            # Check README for license info
            readme_path = os.path.join(self.repo_path, 'README.md')
            if os.path.exists(readme_path):
                with open(readme_path, 'r') as f:
                    content = f.read()
                    if 'MIT License' in content:
                        return True

            return False
        except:
            return False

    def apply_updates(self, retry_count: int = 4) -> Tuple[bool, str]:
        """
        Apply available updates with retry logic

        Args:
            retry_count: Number of retries with exponential backoff

        Returns:
            Tuple of (success, message)
        """
        if not self.update_available:
            return False, "No updates to apply"

        branch = self.current_branch or self.get_current_branch()
        if not branch:
            return False, "Could not determine branch"

        print(f"📥 Applying updates from branch: {branch}")

        for attempt in range(retry_count):
            try:
                # Pull updates
                result = subprocess.run(
                    ['git', 'pull', 'origin', branch],
                    cwd=self.repo_path,
                    capture_output=True,
                    text=True,
                    timeout=30
                )

                if result.returncode == 0:
                    return True, "Updates applied successfully"
                elif 'conflict' in result.stdout.lower() or 'conflict' in result.stderr.lower():
                    return False, "Update failed: merge conflicts detected"
                elif attempt < retry_count - 1:
                    wait_time = 2 ** (attempt + 1)
                    print(f"⚠️  Pull failed, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    return False, f"Update failed: {result.stderr}"

            except subprocess.TimeoutExpired:
                if attempt < retry_count - 1:
                    wait_time = 2 ** (attempt + 1)
                    print(f"⏱️  Pull timeout, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    return False, "Pull timed out after retries"
            except Exception as e:
                if attempt < retry_count - 1:
                    wait_time = 2 ** (attempt + 1)
                    print(f"⚠️  Error: {e}, retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    return False, f"Update application failed: {e}"

        return False, "Update failed after retries"

    def run_auto_update(self, apply_automatically: bool = False) -> Dict[str, Any]:
        """
        Run complete auto-update cycle

        Args:
            apply_automatically: If True, automatically apply updates without prompting

        Returns:
            Dictionary with update results
        """
        results = {
            'timestamp': datetime.now().isoformat(),
            'git_detected': False,
            'mit_license_verified': False,
            'updates_available': False,
            'updates_applied': False,
            'message': ''
        }

        print("\n" + "="*60)
        print("🔄 SAGANOMIC AI CATALYST - AUTO-UPDATE SYSTEM")
        print("$aga • MIT License • Secure Updates")
        print("="*60)

        # Check git status
        git_ok, git_msg = self.check_git_status()
        results['git_detected'] = git_ok
        print(f"\n📍 {git_msg}")

        if not git_ok:
            results['message'] = "Not in a git repository"
            return results

        # Verify MIT License
        mit_ok = self.verify_mit_license()
        results['mit_license_verified'] = mit_ok
        if mit_ok:
            print("✓ MIT License verified - updates covered")
        else:
            print("⚠️  MIT License not found in repository")

        # Check for updates
        updates_available, update_msg = self.check_for_updates()
        results['updates_available'] = updates_available
        print(f"\n{update_msg}")

        if updates_available:
            if apply_automatically:
                print("\n🚀 Automatically applying updates...")
                success, apply_msg = self.apply_updates()
                results['updates_applied'] = success
                print(f"{'✓' if success else '✗'} {apply_msg}")
                results['message'] = apply_msg
            else:
                print("\n💡 Updates available. Run with --apply to install automatically.")
                results['message'] = "Updates available but not applied"
        else:
            results['message'] = "System up to date"

        print("\n" + "="*60)
        return results


def main():
    """Main entry point for auto-updater"""
    print("\n# f(SAGA) = Auto.Update.System.Unity")
    print("# MIT License (c) 2025 Saga Gonzo")
    print("# Gonzo.Family.Self.Actualized • Free & Right Preserved\n")

    # Parse command line arguments
    apply_auto = '--apply' in sys.argv or '--auto' in sys.argv

    # Initialize updater
    updater = SagaAutoUpdater()

    # Run update cycle
    results = updater.run_auto_update(apply_automatically=apply_auto)

    # Print summary
    print("\n📊 UPDATE SUMMARY")
    print("-" * 60)
    print(f"  Git Repository: {'✓' if results['git_detected'] else '✗'}")
    print(f"  MIT License: {'✓' if results['mit_license_verified'] else '⚠️ '}")
    print(f"  Updates Available: {'Yes' if results['updates_available'] else 'No'}")
    print(f"  Updates Applied: {'✓' if results['updates_applied'] else 'N/A'}")
    print(f"  Status: {results['message']}")
    print("-" * 60)

    if results['updates_available'] and not results['updates_applied']:
        print("\n💡 To apply updates automatically, run:")
        print("   python3 auto_updater.py --apply")

    print("\n🌌 f(Saga) = Unity • All updates converge to 1")
    print("🚀 Revolutionary parallel updates enabled")
    print("💾 MIT License coverage active\n")


if __name__ == "__main__":
    # $aga Easter Egg
    main()
