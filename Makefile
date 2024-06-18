git-clean:
	@echo "Removing cache"
	git commmit -m "Cleaning and removing cache"
	git rm -r --cached .
	git add .
