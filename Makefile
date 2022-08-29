all:
	@$(MAKE) -C cv
	@$(MAKE) -C markdown_generator

local:
	bundle install
	bundle exec jekyll serve
